import streamlit as st
from py101 import *
from pandas101 import *

st.sidebar.subheader("About dspy")
st.sidebar.info("**A webapp that is running on python and teaching python!**")
st.sidebar.markdown("""
<img src="https://media.giphy.com/media/3o7527pa7qs9kCG78A/giphy.gif" width="200"><br>
___
## Meet the Team  
**Development and Strategy**
- [Bhanu Chandrika Chitta](https://www.linkedin.com/in/chitta-bhanu-chandrika/)
- [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/)
**Quality Review and Resource Management **
- [Puja Roychowdhury](https://www.linkedin.com/in/pujarc98/)
- [Sneha Podder](http://www.linkedin.com/in/snehapodder)
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

st.subheader("Please select what you would like to do")
features = ["python 101 - Learn the basics of python",
            "pyPrac - Solve problems using python",
            "pandas - Learn data analysis and manipulation",]
selection = st.radio("", features)
st.write("___")
if selection == features[0]:
    st.header("`python 101` - Learn the basics of python")
    st.balloons()
    first()
    helloworld()
    interact()
if selection == features[2]:
    pandas101()
else:
    st.write("![](https://media3.giphy.com/media/STZxU3AXEdwW4caLwS/giphy.gif?cid=790b761115e96593923fc6494cb027cacde63a309c048f29&rid=giphy.gif&ct=g)")


st.markdown("""
___
**© dspy | 2021 | with ❤️ from India**
""")
st.warning("**Development in progress. More features are on the way!**")
