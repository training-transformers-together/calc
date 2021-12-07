models = {}
models['bert-base'] = {}
models['bert-base']['seqlen'] = 512
models['bert-base']['dmodel'] = 768
models['bert-base']['dhid'] = 3072
models['bert-base']['nlayers'] = 12
models['bert-base']['vocab_size'] = 30522


models['bert-large'] = {}
models['bert-large']['seqlen'] = 512
models['bert-large']['dmodel'] = 1024
models['bert-large']['dhid'] = 4096
models['bert-large']['nlayers'] = 24
models['bert-large']['vocab_size'] = 30522

models['t5-3b'] = {}
models['t5-3b']['seqlen'] = 512
models['t5-3b']['dmodel'] = 1024
models['t5-3b']['dhid'] = 16384
models['t5-3b']['nlayers'] = 48
models['t5-3b']['vocab_size'] = 32128

models['t5-11b'] = {}
models['t5-11b']['seqlen'] = 512
models['t5-11b']['dmodel'] = 1024
models['t5-11b']['dhid'] = 64*1024
models['t5-11b']['nlayers'] = 48
models['t5-11b']['vocab_size'] = 32128

models['gpt2-s'] = {}
models['gpt2-s']['seqlen'] = 1024
models['gpt2-s']['dmodel'] = 768
models['gpt2-s']['dhid'] = 768*4
models['gpt2-s']['nlayers'] = 12
models['gpt2-s']['vocab_size'] = 50257

models['gpt2-m'] = {}
models['gpt2-m']['seqlen'] = 1024
models['gpt2-m']['dmodel'] = 1024
models['gpt2-m']['dhid'] = 1024*4
models['gpt2-m']['nlayers'] = 24
models['gpt2-m']['vocab_size'] = 50257

models['gpt2-l'] = {}
models['gpt2-l']['seqlen'] = 1024
models['gpt2-l']['dmodel'] = 1280
models['gpt2-l']['dhid'] = 1280*4
models['gpt2-l']['nlayers'] = 36
models['gpt2-l']['vocab_size'] = 50257

models['gpt2-xl'] = {}
models['gpt2-xl']['seqlen'] = 1024
models['gpt2-xl']['dmodel'] = 1600
models['gpt2-xl']['dhid'] = 1600*4
models['gpt2-xl']['nlayers'] = 48
models['gpt2-xl']['vocab_size'] = 50257

models['gpt3-s'] = {}
models['gpt3-s']['seqlen'] = 2048
models['gpt3-s']['dmodel'] = 768
models['gpt3-s']['dhid'] = 768*4
models['gpt3-s']['nlayers'] = 12
models['gpt3-s']['vocab_size'] = 50257  # from public reimplementations

models['gpt3-m'] = {}
models['gpt3-m']['seqlen'] = 2048
models['gpt3-m']['dmodel'] = 1024
models['gpt3-m']['dhid'] = 1024*4
models['gpt3-m']['nlayers'] = 24
models['gpt3-m']['vocab_size'] = 50257  # from public reimplementations

models['gpt3-l'] = {}
models['gpt3-l']['seqlen'] = 2048
models['gpt3-l']['dmodel'] = 1536
models['gpt3-l']['dhid'] = 1536*4
models['gpt3-l']['nlayers'] = 24
models['gpt3-l']['vocab_size'] = 50257  # from public reimplementations

models['gpt3-xl'] = {}
models['gpt3-xl']['seqlen'] = 2048
models['gpt3-xl']['dmodel'] = 2560
models['gpt3-xl']['dhid'] = 2560*4
models['gpt3-xl']['nlayers'] = 24
models['gpt3-xl']['vocab_size'] = 50257  # from public reimplementations

models['gpt3-3b'] = {}
models['gpt3-3b']['seqlen'] = 2048
models['gpt3-3b']['dmodel'] = 2560
models['gpt3-3b']['dhid'] = 2560*4
models['gpt3-3b']['nlayers'] = 32
models['gpt3-3b']['vocab_size'] = 50257  # from public reimplementations

models['gpt3-7b'] = {}
models['gpt3-7b']['seqlen'] = 2048
models['gpt3-7b']['dmodel'] = 4096
models['gpt3-7b']['dhid'] = 4096*4
models['gpt3-7b']['nlayers'] = 32
models['gpt3-7b']['vocab_size'] = 50257  # from public reimplementations

models['gpt3-13b'] = {}
models['gpt3-13b']['seqlen'] = 2048
models['gpt3-13b']['dmodel'] = 5120
models['gpt3-13b']['dhid'] = 5120*4
models['gpt3-13b']['nlayers'] = 40
models['gpt3-13b']['vocab_size'] = 50257  # from public reimplementations

models['gpt3-175b'] = {}
models['gpt3-175b']['seqlen'] = 2048
models['gpt3-175b']['dmodel'] = 12288
models['gpt3-175b']['dhid'] = 12288*4
models['gpt3-175b']['nlayers'] = 96
models['gpt3-175b']['vocab_size'] = 50257  # from public reimplementations

models['gpt-j-6b'] = {}
models['gpt-j-6b']['seqlen'] = 2048
models['gpt-j-6b']['dmodel'] = 4096
models['gpt-j-6b']['dhid'] = 4096 * 4
models['gpt-j-6b']['nlayers'] = 28
models['gpt-j-6b']['vocab_size'] = 50400

models['dalle-12b'] = {}
models['dalle-12b']['seqlen'] = 1024 + 256
models['dalle-12b']['dmodel'] = 62 * 64
models['dalle-12b']['nlayers'] = 64
models['dalle-12b']['vocab_size'] = 8192 + 16384