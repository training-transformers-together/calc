"""
This specific file was bodged together by ham-handed hedgehogs. If something looks wrong, it's because it is.
If you're not a hedgehog, you shouldn't reuse this code. Use this instead: https://docs.streamlit.io/library/get-started
"""

import streamlit as st


from st_helpers import make_header, content_text, cite
from charts import draw_current_progress

st.set_page_config(page_title="Training Transformers Together", layout="centered")


st.markdown("## Full demo content will be posted here on December 7th!")

make_header()

content_text(f"""
There was a time when you could comfortably train SoTA vision and language models at home on your workstation.
The first ConvNet to beat ImageNet took in 5-6 days on two gamer-grade GPUs{cite("alexnet")}. Today's top-1 imagenet model 
took 20,000 TPU-v3 days{cite("coatnet")}. And things are even worse in the NLP world: training GPT-3 on a top-tier server
 with 8 A100 would still take decades{cite("gpt-3")}.""")

content_text(f"""
So, can individual researchers and small labs still train state-of-the-art? Yes we can!
All it takes is for a bunch of us to come together. In fact, we're doing it right now and <b>you're invited to join!</b>
""", vspace_before=12, vspace_after=16)

draw_current_progress()
