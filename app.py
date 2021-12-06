"""
This specific file was bodged together by ham-handed hedgehogs. If something looks wrong, it's because it is.
If you're not a hedgehog, you shouldn't reuse this code. Use this instead: https://docs.streamlit.io/library/get-started
"""

import streamlit as st

from dashboard_utils.main_metrics import get_main_metrics

st.set_page_config(page_title="Training Transformers Together - Mini-Dashboard", layout="wide")
st.markdown("""<style>
.reportview-container {
    top: -90px;
}
</style>""", unsafe_allow_html=True)
source = get_main_metrics()
st.vega_lite_chart(
    source, {
        "height": 200,
        "title": {"text": "Training DALL-E with volunteers", "dy": 7},
        # ^-- WARNING: do not use long titles, otherwise vega collapses on small screens
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "description": "Current training progress",
        "encoding": {"x": {"field": "wall time", "type": "temporal"}},
        "config": {"axisX": {"labelAngle": -40}},
        "resolve": {"scale": {"y": "independent"}},
        "layer": [
            {
                "mark": {"type": "line", "point": {"tooltip": True, "filled": False, "strokeOpacity": 0},
                         "color": "#85A9C5"},
                "encoding": {
                    "y": {"field": "training loss", "type": "quantitative", "axis": {"titleColor": "#85A9C5"},
                          "scale": {"zero": False}}},
            },
            {
                "mark": {"type": "line", "point": {"tooltip": True, "filled": False, "strokeOpacity": 0.0},
                         "color": "#85C5A6", "opacity": 0.5},
                "encoding": {
                    "y": {"field": "active participants", "type": "quantitative",
                          "axis": {"titleColor": "#85C5A6"}}},
            },
        ],
    },
    use_container_width=True,  # breaks on <600px screens
)
