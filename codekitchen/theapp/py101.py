import streamlit as st

def codearea():
    st.subheader("**Try writing your own codes below!**  \n*P.S. Don't be afraid of errors. Explore as much as you like* 😃")
    st.markdown("""
    <iframe src="https://trinket.io/embed/python/bf50666810" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
    
    """, unsafe_allow_html=True)

def first():
    st.subheader("First things first")
    st.markdown("""
    In order to code, you will need of course, the language itself.  First, let us get our programming languages installed and set up in our systems. To install and get started with python, simply follow the steps here -  \n

    Python documentation - [https://docs.python.org/3/](https://docs.python.org/3/)
    
    Now, we will need an **[Integrated development environment  (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment)** for writing and executing our codes
    There are numerous options available. Few of the commonly used are -
    * [Visual Studio Code ](https://code.visualstudio.com/)
    * [Atom Code Editor ] (https://atom.io/)
    * [PyCharm] (https://www.jetbrains.com/pycharm/)
    * [R Studio](https://www.rstudio.com/products/rstudio/download/) - recommended for coding in R but also supports python 😉
    * [Jupyter Notebook] (https://jupyter.org/)

    💡 Having issues with the above? Try **[Google Colab](https://colab.research.google.com/) **
    """,  unsafe_allow_html=True)

def helloworld():
    st.subheader("The famous hello-world program 😎")
    st.markdown("""
    Welcome to the world of python. In this section, we simply print a string using python code. You can say it's kind of a ritual/tradition for anyone who sets on a journey in coding with any language - our way of saying "Hey world, here I come!" 😉  

    """)
    with st.echo():
        print('Hello World!!')
        print('Get ready to rock-N-roll ')
        # we saw that the lines automatically shifted to new lines.
        # although we can do this manually too, in one print statement
        print('Hello World!! \nGet ready to rock-N-roll')
        # and that's how we do it !!
    response = st.button("Run the above 👆🏻 code")
    if response:
        st.write('Hello World!!')
        st.write('Get ready to rock-N-roll ')
        # we saw that the lines automatically shifted to new lines.
        # although we can do this manually too, in one print statement
        st.write('Hello World!!  \nGet ready to rock-N-roll')
        # and that's how we do it !!
    st.success("Copy the above codes and try them in the code-area below")
    codearea()



# def numbers():
#     with st.echo():
#         x = 30
#         y = 20
#         print(x+y)
    
#     response = st.button("Run this code!")
#     if response:
#         x = 20
#         y = 30
#         st.write(f'Output:  \n{x+y}')

#     
