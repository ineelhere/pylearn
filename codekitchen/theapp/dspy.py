from os import uname
import streamlit as st
from py101 import *
from pandas101 import *
from pyApps import *
from about import *

st.title("`dspy` - Data Science with Python")

st.sidebar.header("""**`DSPY` |**  **Data Science with Python**  \n\n
`dspy` is a free, open-source initiative to help individuals learn/teach the basics of python with streamlit - which also runs on python. 
`dspy` focuses more on the application of python in Data Science.  \n\n
**Please explore the webapp with the options below** 👇
""")

features = ["About dspy",
            "python 101 - Learn the basics of python",
            "pyPrac - Solve problems using python",
            "pyApps - Some simple data apps made with python",
            "pandas - Learn data analysis and manipulation"            
            ]
selection = st.sidebar.radio("", features)
st.sidebar.markdown("""___  
<p align=center><img src="https://media1.giphy.com/media/12TfIo5Mubcb3a/giphy.gif?cid=ecf05e47ua5ndg689hvexiplutidutfo2ncs431840sbp4ib&rid=giphy.gif&ct=g"></p><br>
\n**© dspy | 2021 | with ❤️ from India**""",
unsafe_allow_html=True)
if selection == features[0]:
    about()

if selection == features[1]:
    st.markdown('<img src="https://media3.giphy.com/headers/tiktok/SRLJgKV9HbQK.gif" width="600"><br>', unsafe_allow_html=True)
    st.header("**`python 101` - Learn the basics of python**")
    st.balloons()
    first()
    helloworld()
    interact()
    numbers()
    math_func()

if selection == features[4]:
    pandas101()

if selection == features[2]:
    st.write("![](https://media3.giphy.com/media/STZxU3AXEdwW4caLwS/giphy.gif?cid=790b761115e96593923fc6494cb027cacde63a309c048f29&rid=giphy.gif&ct=g)")

if selection == features[3]:
    pyApps()




st.markdown("""
___

**© dspy | 2021 | with ❤️ from India**
""")
st.warning("**Development in progress. More features are on the way!**")

