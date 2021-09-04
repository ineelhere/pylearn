import streamlit as st
from translate_text import *

def pyApps():
    st.header("**`pyApps` - Some simple data apps made with python**")
    selections = ["Translate text using Python", "Realtime stats on the COVID19 situation in India"]
    st.subheader("**Here are the apps which are available (more on the way!)**")
    response = st.radio('', selections)
    st.markdown("___")

    if response == selections[1]:
        st.success("""
        This webapp is available here - **[https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py](https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py)**
          \nPlease click on the above URL to visit the webapp.
        """)
    if response == selections[0]:
        translate_text()