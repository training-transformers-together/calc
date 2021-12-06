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
({cite("AlexNet", "https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf")})
was trained for 5-6 days on two gamer-grade GPUs. In contrast, today's TOP-1 ImageNet model
({cite("CoAtNet", "https://arxiv.org/abs/2106.04803")})
takes 20,000 TPU-v3 days. And things are even worse in the NLP world: training
{cite("GPT&#8209;3", "https://arxiv.org/abs/2005.14165")} on a top-tier server
with 8x A100 would take decades.""")

content_text(f"""
So, can individual researchers and small labs still train state-of-the-art? Yes we can!
All it takes is for a bunch of us to come together. In fact, we're doing it right now and <b>you're invited to join!</b>
""", vspace_before=12)

draw_current_progress()


content_text(f"""
For this demo we train a model similar to {cite("OpenAI DALL-E", "https://openai.com/blog/dall-e/")},
that is, a transformer "language model" that generates images from text description.
It is trained on {cite("LAION-400M", "https://laion.ai/laion-400-open-dataset/")},
the world's largest openly available image-text-pair dataset with 400 million samples. Our model is based on
the {cite("dalle&#8209;pytorch", "https://github.com/lucidrains/DALLE-pytorch")} implementation
by {cite("Phil Wang", "https://github.com/lucidrains")} with a few tweaks to make it communication-efficient.
""", vspace_after=8)


with st.expander("How to train efficiently over the internet?"):
    content_text(f"""
Modern distributed training algorithms are designed for HPC networks with 10-100 gigabit per second bandwidth.
In turn, a typical Internet connection runs at 10-100 megabits per second: that’s three orders of magnitude slower.
To make distributed training efficient, you need to win back these three orders of magnitude.
This may seem daunting at first, but in reality, DL researchers have already made all the necessary pieces for solving this puzzle:
""")
    content_text(f"""
<table style="border: 0px;"><tbody style="border: 0px;">
<tr><td> Speed&#8209;up <br> </td> <td>How to achieve</td></tr>
<tr><td class=centered><strong>4-16x</strong></td><td>
  <strong>Large-batch training:</strong> {cite("You et al. (2019)", "https://arxiv.org/abs/1904.00962")} proposed a way for training neural networks efficiently with larger batches, and hence, fewer communication rounds.
</td></tr>
<tr><td class=centered><strong>4-64x</strong></td><td>
  <strong>Gradient Compression:</strong> from simple {cite("8-bit quantization", "https://arxiv.org/abs/1511.04561")}
   to advanced techniques such as {cite("Deep Gradient Compression", "https://arxiv.org/abs/1712.01887")}, 
   {cite("PowerSGD", "https://arxiv.org/abs/1905.13727")}, {cite("1-bit Adam", "https://arxiv.org/abs/2102.02888")},
    and many others. As a rule of thumb, you can safely reduce communication by 16-64x. More extreme compression is often
    possible, but it may affect stability or final quality.
</td></tr>
<tr><td class=centered><strong>4-24x</strong></td><td>
   <strong>Parameter sharing:</strong> reusing parameters between model layers results in a model with fewer parameters,
    and hence, fewer gradients to communicate. {cite("Lan et al. (2019)", "https://arxiv.org/abs/1909.11942")} and 
    {cite("Xue et al. (2021)", "https://arxiv.org/pdf/2107.11817.pdf")} propose efficient parameter sharing techniques
    for NLP and vision.
</td></tr>
<tr><td class=centered><strong>1.5-2x</strong></td><td>
   <strong>Overlapping computation with communication:</strong> running network communication in background while
   computing the next portion of gradients. This is a {cite("long-standing trick from HPC", "https://ur.booksc.eu/book/1624068/2d0506")}
    that was recently adapted for DL training. {cite("Ren et al. (2021)", "https://arxiv.org/abs/2101.06840")} show that
     updating parameters in background while computing the next batch of gradients does not reduce convergence.
</td></tr>
</tbody></table>
""")
    content_text("""
    These techniques are already more than enough to cover 1000x slower communication (totalling to 655. 
     and choose which techniques to use. In this demo, we use parameter sharing to reduce the number of parameters by
      roughly 12x. If you don’t want parameter sharing, you can instead use more advanced gradient compression or larger batches.
    """)

content_title("How do I join?")

content_text(f"""
That's easy. First, make sure you're logged in at Hugging Face. If you don't have an account, create one {cite("here", "https://huggingface.co/join")}.<br>

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

make_footer()
