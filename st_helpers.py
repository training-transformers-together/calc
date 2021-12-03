import pathlib

import streamlit as st
import streamlit.components.v1 as components
from bs4 import BeautifulSoup

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


GA_JS = """alert("Hello world!")"""

# Insert the script in the head tag of the static template inside your virtual environement
index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
soup = BeautifulSoup(index_path.read_text(), features="lxml")
if not soup.find(id='custom-js'):
    script_tag = soup.new_tag("script", id='custom-js')
    script_tag.string = GA_JS
    soup.head.append(script_tag)
    index_path.write_text(str(soup))


def make_header():
    components.html(f"<style>{header_style_css}</style>{header_html}<script>{header_animate_js}</script>", height=260)
    st.markdown(meta_html, unsafe_allow_html=True)
    st.markdown(f"<style>{content_style_css}</style>", unsafe_allow_html=True)  # apply css to the rest of the document
    st.markdown('''<script>
                console.log("123");
                var app = document.getElementsByClassName("stApp")[0];
                app.style.height = "99999px";
                </script>''', unsafe_allow_html=True)


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
    CITATIONS[tag] = len(CITATIONS) + 1
    return f"&nbsp;[{CITATIONS[tag]}]"
