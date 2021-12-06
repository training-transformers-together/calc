import streamlit as st

from dashboard_utils.bubbles import get_new_bubble_data
from dashboard_utils.main_metrics import get_main_metrics
from streamlit_observable import observable


def draw_current_progress():
    st.markdown("<br>", unsafe_allow_html=True)
    source = get_main_metrics()

    st.vega_lite_chart(
        source, {
            "height": 200,
            "title": {
                "text": "Training DALL-E with volunteers",
                # ^-- WARNING: do not use long titles, otherwise vega collapses on small screens
                "dy": 6,
            },
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
                        "y": {"field": "training loss", "type": "quantitative", "axis": {"titleColor": "#85A9C5"}}},
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


def draw_participant_bubbles():
    with st.expander("Who's training?", expanded=False):
        st.markdown("### Collaborative training participants\n(may take a few seconds to load)")

        serialized_data, profiles = get_new_bubble_data()
        observable(
            "Participants",
            notebook="d/9ae236a507f54046",  # "@huggingface/participants-bubbles-chart",
            targets=["c_noaws"],
            redefine={"serializedData": serialized_data, "profileSimple": profiles},
        )