import streamlit as st

def about():
    
    
    st.info("**A webapp that is running on python and teaching python!**")
    st.markdown("""
    <img src="https://media.giphy.com/media/3o7527pa7qs9kCG78A/giphy.gif" width="200"><br>
    \n\n`dspy` is an open-source initiative to help individuals learn/teach the basics of python with streamlit - which also runs on python. `dspy` focuses more on the application of python in Data Science.
    \n\nIsn't it nice that one is actually using python to learn/teach python?! This gives an idea of what can be done with python (beyond what has been discussed in this webapp).
    \n\nWe encourage collaborations and usage of this webapp for education/training purposes.
    \n\nFor any queries/feedback please feel free to connect with the team on LinkedIn.
    """, unsafe_allow_html=True)
    
    st.info("""

    Found this interesting?  **[Collaborate here](https://github.com/ineelhere/pylearn/tree/master/codekitchen/theapp)**
 
    """)
    