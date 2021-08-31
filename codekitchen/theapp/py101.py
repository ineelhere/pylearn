import streamlit as st
from streamlit_embedcode import github_gist

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
    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=print%28%27Hello%2520World%21%21%27%29%250Aprint%28%27Get%2520ready%2520to%2520rock-N-roll%2520%27%29%250A%2523%2520we%2520saw%2520that%2520the%2520lines%2520automatically%2520shifted%2520to%2520new%2520lines.%250A%2523%2520although%2520we%2520can%2520do%2520this%2520manually%2520too%252C%2520in%2520one%2520print%2520statement%250Aprint%28%27Hello%2520World%21%21%2520%255CnGet%2520ready%2520to%2520rock-N-roll%27%29%250A%2523%2520and%2520that%27s%2520how%2520we%2520do%2520it%2520%21%21"
    style="width: 612px; height: 238px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>
    """, unsafe_allow_html=True)
    github_gist("https://gist.github.com/bhanuchandrika/8279b541cad6dc9de9d22c2db12147e2", width=800)
    codearea()

def interact():
    st.subheader("Interact with python")
    st.markdown("""
    To do some work, we need something to begin with - right? For example, you need a bat and a ball to play cricket. Similarly, while coding we need some data or input from the user on which we will do some work.
    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=%2523asking%2520user%2520for%2520a%2520text%2520%28name%29%250Ausername%2520%253D%2520input%28%27Please%2520enter%2520your%2520name%2520-%2520%27%29%250A%250A%2523lets%2520greet%2520the%2520user%2520now%250Aprint%2520%28%27Hello%2520%27%2520%252Busername%29%250A%250A%2523ask%2520the%2520user%27s%2520birth%2520year%250Ayear%2520%253D%2520input%28%27Please%2520enter%2520your%2520Birth%2520Year%2520-%2520%27%29%250A%250A%2523calculating%2520the%2520age%252C%2520here%2520we%2520have%2520to%2520change%2520the%2520type%2520for%2520year%2520from%2520string%2520to%2520integer%250Aage%2520%253D%25202021-%2520int%28year%29%250A%250A%2523now%2520we%2520will%2520print%2520the%2520results%250Aprint%28f%27Hey%2520%257Busername%257D%252C%2520You%2520are%2520%257Bage%257D%2520years%2520old%2520%253A%29%2520%27%29%250A%250A%2523using%2520%2522f%2522%2520before%2520writing%2520the%2520print%2520statement%2520saves%2520us%2520a%2520lot%2520of%2520time%2520and%2520effort%250A%2523just%2520need%2520to%2520keep%2520in%2520mind%2520that%2520we%2520are%2520keeping%2520the%2520variables%2520in%2520%257B%257D"
    style="width: 810px; height: 469px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>
    """, unsafe_allow_html=True)    
    github_gist("https://gist.github.com/bhanuchandrika/19633987195c8524a3a1d51f30c9032a", width=800)
    codearea()




   
