"""
This specific file was bodged together by ham-handed hedgehogs. If something looks wrong, it's because it is.
If you're not a hedgehog, you shouldn't reuse this code. Use this instead: https://docs.streamlit.io/library/get-started
"""

import streamlit as st

import mem_calc
from models import models
st.set_page_config(page_title="Memory calculator", layout="wide")
st.markdown("""<style>
.reportview-container {
    top: -80px;
}
</style>""", unsafe_allow_html=True)

models = list(models.keys())  # respect the original order because py37
model = st.selectbox('Model architecture', models, index=models.index("gpt2-l"))

optimizers_names = ('32-bit', '16-bit', '8-bit', 'factorized')
optimizers_values = ['adam', '16-bit-adam', '8-bit-adam', 'adafactor']
optimizer = st.radio('Adam / LAMB states', optimizers_names)
checkpoint = st.checkbox("Gradient checkpointing", value=True)
offload = st.checkbox("Offload optimizer", value=False)
share_params = st.checkbox("Share parameters", value=False)

with st.expander("More options"):

    precisions_names = ('Full', 'Mixed ("O1")', 'Pure 16-bit')
    precisions_values = ('O0', 'O1', 'O3')
    precision = st.selectbox('Precision', precisions_names, index=1)

    vocab_size = int(st.number_input('Vocabulary size', min_value=1, step=1, value=50257, format="%i"))

args = mem_calc.parse_args(f"""
    --model {model} --vocab_size {vocab_size} --optimizer {optimizers_values[optimizers_names.index(optimizer)]}
    {'--checkpoint' if checkpoint else ''} {'--offload' if offload else ''} {'--albert' if share_params else ''}
    --fp16-level {precisions_values[precisions_names.index(precision)]}
""".split())


memory = mem_calc.calculate_memory(args)

cols = st.columns(3)
cols[0].metric("Parameters (GPU)", f"{memory['model']:.2f} GB", f"{memory['model']/memory['total_mem'] * 100:.2f} %", delta_color="off")
cols[1].metric(f"Optimizer ({'GPU' if offload else 'CPU'})", f"{memory['optim']:.2f} GB", f"{memory['optim']/memory['total_mem'] * 100:.2f} %", delta_color="off")
cols[2].metric("Activations (GPU)", f"{memory['grad']:.2f} GB", f"{memory['grad']/memory['total_mem'] * 100:.2f} %", delta_color="off")
cols = st.columns(3)
cols[0].metric("GPU total", f"{memory['total_mem']:.2f} GB")
cols[1].metric("Offloaded to RAM", f"{memory['cpu_mem']:.2f} GB")
cols[2].metric("Communication overhead", f"{memory['overhead'] * 1000:.2f} ms")
