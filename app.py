"""
This specific file was bodged together by ham-handed hedgehogs. If something looks wrong, it's because it is.
If you're not a hedgehog, you shouldn't reuse this code. Use this instead: https://docs.streamlit.io/library/get-started
"""

import streamlit as st


from st_helpers import make_header, content_text, content_title, cite, make_footer, draw_tab_selector
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
""", vspace_before=12)

draw_current_progress()

content_text(f"""
The model we're training is called DALLE: a transformer "language model" that generates images from text description.
We're training this model on <a target="_blank" rel="noopener noreferrer" href=https://laion.ai/laion-400-open-dataset/>LAION</a> - the world's largest openly available
image-text-pair dataset with 400 million samples. Our model is based on
<a target="_blank" rel="noopener noreferrer" href=https://github.com/lucidrains/DALLE-pytorch>dalle-pytorch</a> 
with several tweaks for memory-efficient training.""")


content_title("How do I join?")

content_text("""
That's easy. First, make sure you're logged in at Hugging Face. If you don't have an account, create one <b>TODO</b>.<br>

<ul style="text-align: left; list-style-position: inside; margin-top: 12px; margin-left: -32px;">
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

content_title("But how does it work?")
content_text("<b> TODO </b> General Story That Weaves Together Three Tabs Below . Lorem ipsum dolor sit amet, "
             "consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim"
             " ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
             "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
             "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

query_params = st.experimental_get_query_params()
tabs = ["Efficient Training", "Security & Privacy", "Make Your Own (TBU)"]
active_tab = query_params["tab"][0] if "tab" in query_params else tabs[0]
if active_tab not in tabs:
    st.experimental_set_query_params(tab=tabs[0])
    active_tab = tabs[0]

draw_tab_selector(tabs, active_tab)

if active_tab == tabs[0]:
    content_text("<b> TODO 1</b> Lorem ipsum dolor sit amet, "
                 "consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim"
                 " ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                 "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
                 "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

elif active_tab == tabs[1]:
    content_text("<b> TODO 2</b> Lorem ipsum dolor sit amet, "
                 "consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim"
                 " ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                 "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
                 "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

elif active_tab == tabs[2]:
    content_text("<b> TODO 3</b> Lorem ipsum dolor sit amet, "
                 "consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim"
                 " ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                 "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
                 "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

else:
    st.error("Something has gone terribly wrong. Please keep your fingers crossed while reloading the page.")


content_text("<b> TODO UPDATE")
make_footer()
