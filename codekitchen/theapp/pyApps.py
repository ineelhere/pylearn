import streamlit as st
from translate_text import *

def pyApps():
    st.header("**`pyApps` - Some simple data apps made with python**")
    selections = ["Translate text using Python"]
    st.subheader("**Here are the apps which are available (more on the way!)**")
    response = st.radio('', selections)
    st.markdown("___")

    if response == selections[0]:
        translate_text()