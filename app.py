import os

import streamlit as st
import wandb

from dashboard_utils.bubbles import get_new_bubble_data
from dashboard_utils.main_metrics import get_main_metrics
from streamlit_observable import observable

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Training Transformers Together", layout="centered")
with open("static/header.html", 'r', encoding='utf-8') as f:
    header_html = f.read()
with open("static/header_style.css", 'r', encoding='utf-8') as f:
    header_style_css = f.read()
with open("static/header_animate.js") as f:
    header_animate_js = f.read()
with open("static/content_style.css", 'r', encoding='utf-8') as f:
    content_style_css = f.read()
with open("static/meta.html", 'r', encoding='utf-8') as f:
    meta_html = f.read()

st.markdown("## Full demo content will be posted here on December 7th!")

components.html(f"<style>{header_style_css}</style>{header_html}<script>{header_animate_js}</script>", height=260)

st.markdown(meta_html, unsafe_allow_html=True)
st.markdown(f"<style>{content_style_css}</style>", unsafe_allow_html=True)  # apply css to the rest of the document

def content_text(text: str, vspace: int = 0):
    st.markdown(f'<center><div class="padded faded main_text" style="padding-top: {vspace}px;">{text}</div><center>',
                unsafe_allow_html=True)
CITATIONS = {}
def cite(tag):
    CITATIONS[tag] = len(CITATIONS) + 1
    return f"[{CITATIONS[tag]}]"

content_text(f"""
There was a time when you could comfortably train SoTA vision and language models at home on your workstation.
The first ConvNet to beat ImageNet took in 5-6 days on two gamer-grade GPUs {cite("alexnet")}. Today's top-1 imagenet model 
took 20,000 TPU-v3 days {cite("coatnet")}. And things are even worse in the NLP world: training GPT-3 on a top-tier server
 with 8 A100 would still take decades {cite("gpt-3")} .""")

content_text(f"""
So, can individual researchers and small labs still train state-of-the-art? Yes we can!
All it takes is for a bunch of us to come together. In fact, we're doing it right now and <b>you're invited to join!</b>
""", vspace=12)

st.markdown("<br>", unsafe_allow_html=True)

source = get_main_metrics()
st.vega_lite_chart(
    source, {
        "height": 200,
        "title": "Training DALLE with volunteers. Updated every few minutes during NeurIPS.",
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "description": "Current training progress",
        "encoding": {"x": {"field": "date", "type": "temporal"}},
        "config": {"axisX": {"labelAngle": -40}},
        "resolve": {"scale": {"y": "independent"}},
        "layer": [
            {
                "mark": {"type": "line", "point": {"tooltip": True, "filled": False, "strokeOpacity": 0},
                         "color": "#85A9C5"},
                "encoding": {"y": {"field": "training loss", "type": "quantitative", "axis": {"titleColor": "#85A9C5"}}},
            },
            {
                "mark": {"type": "line", "point": {"tooltip": True, "filled": False, "strokeOpacity": 0.0},
                         "color": "#85C5A6", "opacity": 0.5},
                "encoding": {
                    "y": {"field": "active participants", "type": "quantitative", "axis": {"titleColor": "#85C5A6"}}},
            },
        ],
    },
    use_container_width=True,
)

#
# st.caption("Number of alive runs over time")
# st.vega_lite_chart(
#     source,
#     use_container_width=True,
# )
# st.caption("Number of steps")
# st.vega_lite_chart(
#     source,
#     {
#         "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
#         "description": "Training Loss",
#         "mark": {"type": "line", "point": {"tooltip": True, "filled": False, "strokeOpacity": 0}},
#         "encoding": {"x": {"field": "date", "type": "temporal"}, "y": {"field": "steps", "type": "quantitative"}},
#         "config": {"axisX": {"labelAngle": -40}},
#     },
#     use_container_width=True,
# )
#
# st.header("Collaborative training participants")
# serialized_data, profiles = get_new_bubble_data()
# observable(
#     "Participants",
#     notebook="d/9ae236a507f54046",  # "@huggingface/participants-bubbles-chart",
#     targets=["c_noaws"],
#     redefine={"serializedData": serialized_data, "profileSimple": profiles},
# )
