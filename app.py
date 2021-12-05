"""
This specific file was bodged together by ham-handed hedgehogs. If something looks wrong, it's because it is.
If you're not a hedgehog, you shouldn't reuse this code. Use this instead: https://docs.streamlit.io/library/get-started
"""

import streamlit as st


from st_helpers import make_header, content_text, content_title, cite, make_footer, make_tabs
from charts import draw_current_progress

st.set_page_config(page_title="Training Transformers Together", layout="centered")


st.markdown("## Full demo content will be posted here on December 7th!")

make_header()

content_text(f"""
There was a time when you could comfortably train state-of-the-art vision and language models at home on your workstation.
The first convolutional neural net to beat ImageNet
(<a target="_blank" href="https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf">AlexNet</a>)
was trained for 5-6 days on two gamer-grade GPUs. In contrast, today's TOP-1 ImageNet model
(<a target="_blank" href="https://arxiv.org/abs/2106.04803">CoAtNet</a>)
takes 20,000 TPU-v3 days. And things are even worse in the NLP world: training
<a target="_blank" href="https://arxiv.org/abs/2005.14165">GPT&#8209;3</a> on a top-tier server
with 8x A100 would take decades.""")

content_text(f"""
So, can individual researchers and small labs still train state-of-the-art? Yes we can!
All it takes is for a bunch of us to come together. In fact, we're doing it right now and <b>you're invited to join!</b>
""", vspace_before=12)

draw_current_progress()

content_text(f"""
We're training a model similar to <a target="_blank" href="https://openai.com/blog/dall-e/">OpenAI DALL-E</a>,
that is, a transformer "language model" that generates images from text description.
It is trained on <a target="_blank" href=https://laion.ai/laion-400-open-dataset/>LAION-400M</a>,
the world's largest openly available image-text-pair dataset with 400 million samples. Our model is based on
the <a target="_blank" href=https://github.com/lucidrains/DALLE-pytorch>dalle&#8209;pytorch</a> implementation
by <a target="_blank" href="https://github.com/lucidrains">Phil Wang</a> with several tweaks for memory-efficient training.""")


content_title("How do I join?")

content_text("""
That's easy. First, make sure you're logged in at Hugging Face. If you don't have an account, create one <b>TODO</b>.<br>

<ul style="text-align: left; list-style-position: inside; margin-top: 12px; margin-left: -24px;">
    <li style="margin-top: 4px;">
        Join our organization on Hugging Face here: <b>TODO</b>. </li>
    <li style="margin-top: 4px;">
        The simplest way to start is with colab <b>TODO</b>;</li>
    <li style="margin-top: 4px;">
        You can find other starter kits, evaluation and inference notebooks <b>TODO IN OUR ORGANIZATION</b>;</li>
    <li style="margin-top: 4px;">
        If you have any issues, <b>TODO DISCORD BADGE</b> </li>
</ul>

Please note that we currently limit the number of colab participants to <b>TODO</b> to make sure we do not interfere
with other users. If there are too many active peers, take a look at alternative starter kits here <b>TODO</b>
""")

content_title("How does it work?")
content_text("<b> TODO </b> General Story That Weaves Together Three Tabs Below . Lorem ipsum dolor sit amet, "
             "consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim"
             " ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
             "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
             "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

make_tabs()

content_text("<b> TODO UPDATE")
make_footer()
