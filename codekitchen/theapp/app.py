import streamlit as st

st.sidebar.subheader("About dspy")
st.sidebar.info("A webapp that is running on python and teaching python!")
st.sidebar.markdown("""
<img src="https://media.giphy.com/media/3o7527pa7qs9kCG78A/giphy.gif" width="200">
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
if selection == features[0]:
    st.balloons()
else:
    st.write("![](https://media3.giphy.com/media/STZxU3AXEdwW4caLwS/giphy.gif?cid=790b761115e96593923fc6494cb027cacde63a309c048f29&rid=giphy.gif&ct=g)")
