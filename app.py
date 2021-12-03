"""
This specific file was bodged together by ham-handed hedgehogs. If something looks wrong, it's because it is.
If you're not a hedgehog, you shouldn't reuse this code. Use this instead: https://docs.streamlit.io/library/get-started
"""

import streamlit as st


from st_helpers import make_header, content_text, content_title, cite
from charts import draw_current_progress

st.set_page_config(page_title="Training Transformers Together", layout="centered")


st.markdown("## Full demo content will be posted here on December 7th!")

make_header()


from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import Figure, output_file, show
x = [x*0.005 for x in range(0, 200)]
y = x
source = ColumnDataSource(data=dict(x=x, y=y))

plot = Figure(width=400, height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
    const data = source.data;
    const f = cb_obj.value
    const x = data['x']
    const y = data['y']
    for (let i = 0; i < x.length; i++) {
        y[i] = Math.pow(x[i], f)
    }
    source.change.emit();
    alert("123");
""")

slider = Slider(start=0.1, end=4, value=1, step=.1, title="power")
slider.js_on_change('value', callback)

layout = column(slider, plot)
st.bokeh_chart(layout)

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

content_text(f"""
The model we're training is called DALLE: a transformer "language model" that generates images from text description.
We're training this model on <a href=https://laion.ai/laion-400-open-dataset/>LAION</a> - the world's largest openly available
image-text-pair dataset with 400 million samples.
<b>TODO</b> You see a short description of training dataset, model architecture and training configuration.
In includes all necessary citations and, most importantly, a down-to-earth explanation of what exactly is dalle.
It properly refers the communities that provided data, the source codebase and provides necessary links.
""")

content_title("How do I join?")

content_text("For the sake of ")

