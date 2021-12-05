from typing import Sequence

import streamlit as st
import streamlit.components.v1 as components

with open("static/header.html", 'r', encoding='utf-8') as f:
    header_html = f.read()
with open("static/header_style.css", 'r', encoding='utf-8') as f:
    embeds_style_css = f.read()
with open("static/header_animate.js") as f:
    header_animate_js = f.read()
with open("static/content_style.css", 'r', encoding='utf-8') as f:
    content_style_css = f.read()
with open("static/meta.html", 'r', encoding='utf-8') as f:
    meta_html = f.read()
with open("static/tabs.html", 'r', encoding='utf-8') as f:
    tabs_html = f.read()
with open("static/footer.html", 'r', encoding='utf-8') as f:
    footer_html = f.read()


def make_header():
    components.html(f"<style>{embeds_style_css}</style>{header_html}<script>{header_animate_js}</script>", height=260)
    st.markdown(meta_html, unsafe_allow_html=True)
    st.markdown(f"<style>{content_style_css}</style>", unsafe_allow_html=True)  # apply css to the rest of the document
    st.markdown(
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
        unsafe_allow_html=True,
    )


def make_tabs():
    components.html(f"{tabs_html}", height=1000, scrolling=True)


def make_footer():
    components.html(f"<style>{content_style_css}</style>{footer_html}", height=110)


def content_title(title: str, vspace_before: int = 0, vspace_after: int = 0):
    st.markdown(f'<center><div class="padded faded demo_title" '
                f'style="padding-top: {vspace_before}px; padding-bottom: {vspace_after}px; text-align: justify;">'
                f'{title}</div><center>',
                unsafe_allow_html=True)


def content_text(text: str, vspace_before: int = 0, vspace_after: int = 0):
    st.markdown(f'<center><div class="padded faded demo_text" '
                f'style="padding-top: {vspace_before}px; padding-bottom: {vspace_after}px; text-align: justify;">'
                f'{text}</div><center>',
                unsafe_allow_html=True)


CITATIONS = {}


def cite(tag):
    CITATIONS.setdefault(tag, len(CITATIONS) + 1)
    return f"&nbsp;[{CITATIONS[tag]}]"
