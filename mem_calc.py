import argparse
import math
from models import models


def get_GB(nbytes):
    return nbytes/(1024**3)


def vocab(bsz, seqlen, dmodel, vocab_dim):
    # assumes tied embeddings

    w = vocab_dim*dmodel
    emb = seqlen*bsz*dmodel
    emb_norm = seqlen*bsz*dmodel
    pos_emb = seqlen*bsz*dmodel
    out_emb = seqlen*bsz*vocab_dim
    softmax_emb = seqlen*bsz*vocab_dim

    model = w + dmodel
    grad = emb + emb_norm + pos_emb + out_emb + softmax_emb
    grad *= 1
    return model, grad


def transformer(bsz, seqlen, dmodel, nlayers, vocab_type, dhid=None,
                checkpoint=False, shared_groups=None):
    if dhid is None: dhid = 4*dmodel
    model = 0
    grad = 0
    for i in range(nlayers):
        m, g = transformer_layer(bsz, seqlen, dmodel, dhid, checkpoint=checkpoint)
        model += m
        grad += g

    if shared_groups is not None:
        model = model / nlayers * shared_groups

    m, g = vocab(bsz, seqlen, dmodel, vocab_type)
    model += m
    grad += g

    return model, grad

def layer_norm(bsz, seqlen, dmodel):
    w = dmodel
    x_grad = bsz*seqlen*dmodel
    return w, x_grad


def transformer_layer(bsz, seqlen, dmodel, dhid, checkpoint=False):
    model = 0
    grad = 0

    m, g = ffn(bsz, seqlen, dmodel, dhid, 'gelu')
    model += m
    grad += g*3

    m, g = attention_layer(bsz, seqlen, dmodel)
    model += m
    grad += g*5.0

    m, g = layer_norm(bsz, seqlen, dmodel)
    model += m
    grad += g*1.0

    if checkpoint:
        grad = bsz * seqlen * dmodel

    return model, grad

def attention_layer(bsz, seqlen, dmodel):
    w_proj = dmodel*3*dmodel
    w_out = dmodel*dmodel

    x_residual = bsz*seqlen*dmodel
    x_proj = bsz*seqlen*dmodel*3
    #x_proj_contiguous = bsz*seqlen*dmodel*3
    x_proj_contiguous = 0

    x_qscaled = bsz*seqlen*dmodel
    x_qk = bsz*seqlen*seqlen*2 # we need to store both input sequence directions for gradient computation
    x_softmax = bsz*seqlen*seqlen
    x_softmax_v = bsz*seqlen*dmodel*2 # we need to store both input sequence directions for gradient computation
    #x_out_contiguous = bsz*seqlen*dmodel
    x_out_contiguous = 0
    x_out = bsz*seqlen*dmodel

    model = w_proj + w_out
    grad = x_residual + x_proj + x_proj_contiguous + x_qscaled + x_qk + x_softmax + x_softmax_v + x_out_contiguous + x_out
    return model, grad



def ffn(bsz, seqlen, dmodel, dhid, func='relu'):
    # out = linear(relu(linear(x), inplace=True)) + x
    w1 = dmodel*dhid
    w2 = dhid*dmodel
    model = w1 + w2
    wgrad = model
    x1 = bsz*seqlen*dhid
    if func != 'relu': x1 *= 2 # inplace not possible with most other functions
    x2 = bsz*seqlen*dmodel
    residual = bsz*seqlen*dmodel
    grad = x1 + x2 + residual

    return model, grad


OPTIMIZERS = ['adam', 'adafactor', 'adafactor-fac-only', '8-bit-adam', '16-bit-adam']


def parse_args(args=None):
    parser = argparse.ArgumentParser('Memory calculator')

    parser.add_argument('--nlayers', type=int, help='The number of transformer layers.')
    parser.add_argument('--bsz', type=int, default=1, help='The batch size. Default: 2')
    parser.add_argument('--seqlen', type=int, help='The sequence length.')
    parser.add_argument('--dmodel', type=int, help='The core model size.')
    parser.add_argument('--dhid', type=int, default=None,
                        help='The hidden size of the FFN layer. Default: 4x model size.')
    parser.add_argument('--fp16-level', type=str, default='O1',
                        help='FP16-level to use. O0 = FP32; O1 = mixed-precision (16+32); O3 = fp16. Default: O1.')
    parser.add_argument('--model', default='', choices=list(models.keys()), help='Predefined NLP transformer models')
    parser.add_argument('--optimizer', default='adam', choices=OPTIMIZERS, help='The optimizer to use.')
    parser.add_argument('--vocab_size', type=int, default=None, help='The vocabulary to use.')
    parser.add_argument('--offload', action='store_true', help='Whether to use optimizer offload.')
    parser.add_argument('--ngpus', type=int, default=1, help='The number of gpus. Default: 1')
    parser.add_argument('--zero', type=int, default=0,
                        help='The ZeRO level (1 optimizer, 2 optimizer+weights, 3 everything. Default: 1')
    parser.add_argument('--shared_groups', type=int, default=None, help='Number of shared layer groups (as in ALBERT). Defaults to no sharing.')
    parser.add_argument('--checkpoint', action='store_true', help='Use gradient checkpointing.')

    return parser.parse_args(args)


def calculate_memory(args):
    if args.model != '':
        if args.model not in models:
            raise ValueError(f'{args.model} is not supported')
        else:
            for key, value in models[args.model].items():
                if getattr(args, key, None) is None:
                    setattr(args, key, value)

    model, grad = transformer(args.bsz, args.seqlen, args.dmodel, args.nlayers, args.vocab_size, args.dhid, args.checkpoint, args.shared_groups)
    parameters = model

    if args.optimizer == 'adam':
        optim = 8*model
    elif args.optimizer == '8-bit-adam':
        optim = 2*model
    elif args.optimizer in ['16-bit-adam', 'adafactor']:
        optim = 4*model
    elif args.optimizer in ['adafactor-fac-only']:
        optim = math.log(model)

    if args.fp16_level == 'O0':
        # fp32 weights
        wgrad = 4*model
        model = 4*model
        grad = 4*grad # fp32
    elif args.fp16_level in ['O1', 'O2']:
        # fp16 weights + fp32 master weights
        wgrad = 2*model
        model = 4*model + (2*model)
        grad = 2*grad # fp16
    elif args.fp16_level == 'O3':
        wgrad = 2*model
        model = 2*model #fp16
        grad = 2*grad # fp32

    model = get_GB(model)
    grad = get_GB(grad)
    optim = get_GB(optim)
    wgrad = get_GB(wgrad)

    cpu_mem = 0
    overhead = 0

    if args.zero == 1:
        if not args.offload:
            # assumes PCIe 4.0 infiniband (200 Gbit/s = 25 GB/s)
            overhead += optim/25

        optim = optim / args.ngpus
    elif args.zero == 2:
        if not args.offload:
            # assumes PCIe 4.0 infiniband (200 Gbit/s = 25 GB/s)
            overhead += optim/25
            overhead += wgrad/25

        optim = optim / args.ngpus
        wgrad = wgrad / args.ngpus
    elif args.zero == 3:
        if not args.offload:
            # assumes PCIe 4.0 infiniband (200 Gbit/s = 25 GB/s)
            overhead += optim/25
            overhead += model/25
            overhead += wgrad/25

        optim = optim / args.ngpus
        model = model / args.ngpus
        wgrad = wgrad / args.ngpus


    if args.offload:
        cpu_mem = optim + wgrad
        optim = 0
        wgrad = 0
        if args.ngpus <= 2:
            # 12 GB/s for PCIe 3.0 and 1-2x GPU setup (16 lanes, 16 GB/s theoretical)
            overhead = cpu_mem/12
        else:
            # 6 GB/s for PCIe 3.0 and 4x GPU setup
            overhead = cpu_mem/6


    total_mem = model + grad + optim + wgrad
    return locals()


if __name__ == '__main__':
    args = parse_args()
    mem = calculate_memory(args)
    print('')
    print(f'Model: {args.model} with batch size {args.bsz} and sequence length {args.seqlen} and a total of {mem["parameters"]/1e9:.4f}B parameters.')
    print('='*80)
    print('Weight memory:           {0:.2f} GB ({1:.2f}%)'.format(mem['model'], 100*mem['model']/mem['total_mem']))
    print('Weight gradient memory:  {0:.2f} GB ({1:.2f}%)'.format(mem['wgrad'], 100*mem['wgrad']/mem['total_mem']))
    print('Input gradient memory:   {0:.2f} GB ({1:.2f}%)'.format(mem['grad'], 100*mem['grad']/mem['total_mem']))
    print('Optimizer memory:        {0:.2f} GB ({1:.2f}%)'.format(mem['optim'], 100*mem['optim']/mem['total_mem']))
    print('Total GPU memory:        {0:.2f} GB'.format(mem['total_mem']))
    if mem['cpu_mem'] > 0:
        print('Total CPU memory:        {0:.2f} GB'.format(mem['cpu_mem']))
    if mem['overhead'] > 0:
        print('Overhead: {0:.2f} seconds per update (can be partially overlapped with compute)'.format(mem['overhead']))
