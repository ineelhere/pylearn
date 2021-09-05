import streamlit as st
from py101 import *
from pandas101 import *
from pyApps import *

st.sidebar.subheader("About dspy")
st.sidebar.info("**A webapp that is running on python and teaching python!**")
st.sidebar.markdown("""
<img src="https://media.giphy.com/media/3o7527pa7qs9kCG78A/giphy.gif" width="200"><br>
  \n\n`dspy` is an open-source initiative to help individuals learn/teach the basics of python with streamlit - which also runs on python. `dspy` focuses more on the application of python in Data Science.
  \n\nIsn't it nice that one is actually using python to learn/teach python?! This gives an idea of what can be done with python (beyond what has been discussed in this webapp).
  \n\nWe encourage collaborations and usage of this webapp for education/training purposes.
  \n\nFor any queries/feedback please feel free to connect with the team on LinkedIn.
___

Found this interesting?  \n
**[Collaborate here](https://github.com/ineelhere/pylearn/tree/master/codekitchen/theapp)**
___
**© dspy | 2021 | with ❤️ from India**
""", unsafe_allow_html=True)

st.title("`dspy` - Data Science with Python")
st.markdown("""
___
""")

st.header("**Please `select` what you would like to do**")
features = ["python 101 - Learn the basics of python",
            "pyPrac - Solve problems using python",
            "pyApps - Some simple data apps made with python",
            "pandas101 - Learn data analysis and manipulation",
            ]
selection = st.radio("", features)
st.write("___")
if selection == features[0]:
    st.header("**`python 101` - Learn the basics of python**")
    st.balloons()
    first()
    helloworld()
    interact()

if selection == features[3]:
    pandas101()

if selection == features[1]:
    st.write("![](https://media3.giphy.com/media/STZxU3AXEdwW4caLwS/giphy.gif?cid=790b761115e96593923fc6494cb027cacde63a309c048f29&rid=giphy.gif&ct=g)")

if selection == features[2]:
    pyApps()

st.markdown("""
___
**© dspy | 2021 | with ❤️ from India**
""")
st.warning("**Development in progress. More features are on the way!**")

