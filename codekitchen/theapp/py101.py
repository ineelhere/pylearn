import streamlit as st
from streamlit_embedcode import github_gist

def codearea():
    st.markdown("""
    *Try writing your own codes in Google Colab notebooks 👉 *
    <a href="https://colab.research.google.com/" target="_blank"><img width="64" height="64" src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="Github" > </a>
    
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

# def helloworld():
#     st.subheader("**The famous hello-world program 😎**")
#     st.markdown("""
#     Welcome to the world of python. In this section, we simply print a string using python code. You can say it's kind of a ritual/tradition for anyone who sets on a journey in coding with any language - our way of saying "Hey world, here I come!" 😉  
#     <iframe
#     src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=print%28%27Hello%2520World%21%21%27%29%250Aprint%28%27Get%2520ready%2520to%2520rock-N-roll%2520%27%29%250A%2523%2520we%2520saw%2520that%2520the%2520lines%2520automatically%2520shifted%2520to%2520new%2520lines.%250A%2523%2520although%2520we%2520can%2520do%2520this%2520manually%2520too%252C%2520in%2520one%2520print%2520statement%250Aprint%28%27Hello%2520World%21%21%2520%255CnGet%2520ready%2520to%2520rock-N-roll%27%29%250A%2523%2520and%2520that%27s%2520how%2520we%2520do%2520it%2520%21%21"
#     style="width: 612px; height: 238px; border:0; transform: scale(1); overflow:hidden;"
#     sandbox="allow-scripts allow-same-origin">
#     </iframe>
#     """, unsafe_allow_html=True)
#     github_gist("https://gist.github.com/ineelhere/45f65381b6947026c90f4bc8476bc351", width=800, height=300)
#     codearea()

# def interact():
#     st.subheader("**Interact with python**")
#     st.markdown("""
#     To do some work, we need something to begin with - right? For example, you need a bat and a ball to play cricket. Similarly, while coding we need some data or input from the user on which we will do some work.
#     <iframe
#     src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=%2523asking%2520user%2520for%2520a%2520text%2520%28name%29%250Ausername%2520%253D%2520input%28%27Please%2520enter%2520your%2520name%2520-%2520%27%29%250A%250A%2523lets%2520greet%2520the%2520user%2520now%250Aprint%2520%28%27Hello%2520%27%2520%252Busername%29%250A%250A%2523ask%2520the%2520user%27s%2520birth%2520year%250Ayear%2520%253D%2520input%28%27Please%2520enter%2520your%2520Birth%2520Year%2520-%2520%27%29%250A%250A%2523calculating%2520the%2520age%252C%2520here%2520we%2520have%2520to%2520change%2520the%2520type%2520for%2520year%2520from%2520string%2520to%2520integer%250Aage%2520%253D%25202021-%2520int%28year%29%250A%250A%2523now%2520we%2520will%2520print%2520the%2520results%250Aprint%28f%27Hey%2520%257Busername%257D%252C%2520You%2520are%2520%257Bage%257D%2520years%2520old%2520%253A%29%2520%27%29%250A%250A%2523using%2520%2522f%2522%2520before%2520writing%2520the%2520print%2520statement%2520saves%2520us%2520a%2520lot%2520of%2520time%2520and%2520effort%250A%2523just%2520need%2520to%2520keep%2520in%2520mind%2520that%2520we%2520are%2520keeping%2520the%2520variables%2520in%2520%257B%257D"
#     style="width: 810px; height: 469px; border:0; transform: scale(1); overflow:hidden;"
#     sandbox="allow-scripts allow-same-origin">
#     </iframe>
#     """, unsafe_allow_html=True)    
#     github_gist("https://gist.github.com/ineelhere/d4a32717597eb2c89a7e68d1a06e07b7", width=800, height=500)
#     codearea()

# def numbers():
#     st.subheader("**Deal with numbers**")
#     st.markdown("""
#     So, in programming you can do lots of mathematical operations. But for that you need to have an idea of what are the various datatypes that are to be considered - or even not considered! This section will introduce with some of the possibilities and we'll cover the other complex stuff as we progress.
#     <br><br>You've got it. Keep going! 🙂  
#     <iframe
#     src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=panda-syntax&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=%2523%2520first%2520let%2520us%2520understand%2520the%2520datatypes.%250A%250A%2523%2520integer%2520datatype%250Aprint%28f%2522The%2520datatype%2520for%2520variable%252020%2520is%2520%257Btype%2820%29%257D%2522%29%2520%2523%2520%253Cclass%2520%27int%27%253E%250A%250A%2523%2520float%2520datatype%250Aprint%28f%2522The%2520datatype%2520for%2520variable%252020.02%2520is%2520%257Btype%2820.02%29%257D%2522%29%2520%2523%2520%253Cclass%2520%27float%27%253E%250A%250A%2523%2520string%2520datatype%250Aprint%28f%2522The%2520datatype%2520for%2520variable%2520%27abcd%2520efg%2520hijk%2520lmnop%27%2520is%2520%257Btype%28%27abcd%2520efg%2520hijk%2520lmnop%27%29%257D%2522%29%2520%2523%253Cclass%2520%27str%27%253E%250A%250A%2523get%2520the%2520binary%2520for%2520the%2520number%250Aprint%28bin%282020%29%29%2520%2523prints%2520the%2520binary%2520form%2520of%25202020%2520which%2520is%25200b11111100100%250A%2523get%2520number%28integer%29%2520from%2520binary%2520form%250Aprint%28int%28%270b11111100100%27%252C%25202%29%29%2520%2523%25202%2520for%2520printing%2520the%2520integer%2520form%2520by%2520base%2520as%25202%250A%250A%2523%2520----------------%2520that%2520would%2520be%2520enogh%2520for%2520now%2520to%2520understand%2520about%2520the%2520datatypes.%250A%250A%2523%2520Let%2520us%2520now%2520perform%2520some%2520arithmetic%2520operations%250A%250A%2523arithmetic%2520operations%2520without%2520variables%250Aprint%28f%2522Sum%2520of%25203%2520and%25205%2520is%2520%257B3%252B5%257D%2522%29%250Aprint%28f%2522difference%2520of%25203%2520and%25205%2520is%2520%257B3-5%257D%2522%29%250Aprint%28f%2522Product%2520of%25203%2520and%25205%2520is%2520%257B3*5%257D%2522%29%250Aprint%28f%2522Fraction%2520or%2520Division%2520of%25203%2520and%25205%2520is%2520%257B3%252F5%257D%2522%29%250Aprint%28f%2522exponent%2520of%25203%2520with%25205%2520is%2520%257B3**5%257D%2522%29%2520%2523exponent%250Aprint%28f%2522Modulus%2520of%25203%2520and%25205%2520is%2520%257B3%25255%257D%2522%29%2523mod%250A%250A%2523arithmetic%2520operations%2520with%2520variables%250A%250Aa%2520%253D%2520input%28%2522Enter%2520a%2520number.%2520It%2520will%2520be%2520stored%2520as%2520%27a%27%2520%253D%2520%2522%29%250Ab%2520%253D%2520input%28%2522Enter%2520another%2520number.%2520It%2520will%2520be%2520stored%2520as%2520%27b%27%2520%253D%2520%2522%29%250A%2523python%2520accepts%2520inputs%2520as%2520str.%2520So%2520whenever%2520we%2520need%2520to%2520perform%2520any%2520mathematical%2520operations%252C%2520we%2520need%2520to%2520change%2520the%2520datatypes%250A%250Aprint%28f%2522You%2520see%252C%2520I%2520am%2520writing%2520here%2520a%252Bb%2520but%2520the%2520output%2520will%2520not%2520be%2520the%2520sum.%2520%255CnInstead%252C%2520you%2520will%2520see%2520the%2520two%2520numbers%2520will%2520be%2520concatenated%21%2520%255CnHere%2520is%2520the%2520output%2520%253D%2520%257Ba%252Bb%257D%2522%29%250A%250Aa%2520%253D%2520float%28a%29%2520%2523keeping%2520in%2520float%2520is%2520safer%2520as%2520user%2520might%2520feed%2520data%2520with%2520decimals%250Ab%2520%253D%2520float%28b%29%2520%2523keeping%2520in%2520float%2520is%2520safer%2520as%2520user%2520might%2520feed%2520data%2520with%2520decimals%250A%250Aprint%28f%2522Sum%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba%252Bb%257D%2522%29%250Aprint%28f%2522difference%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba-b%257D%2522%29%250Aprint%28f%2522Product%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba*b%257D%2522%29%250Aprint%28f%2522Fraction%2520or%2520Division%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba%252Fb%257D%2522%29%250Aprint%28f%2522exponent%2520of%2520%257Ba%257D%2520with%2520%257Bb%257D%2520is%2520%257Ba**b%257D%2522%29%2520%2523exponent%250Aprint%28f%2522Modulus%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba%2525b%257D%2522%29%2523mod"
#     style="width: 810px; height: 469px; border:0; transform: scale(1); overflow:hidden;"
#     sandbox="allow-scripts allow-same-origin">
#     </iframe>
#     """, unsafe_allow_html=True)
#     github_gist("https://gist.github.com/ineelhere/13b6a1592d14ca05ef74b681803d65ed", width=800, height=500)
#     codearea()

# def math_func():
#     st.subheader("**Math Functions**")
#     st.markdown("""
#     To make our lives easier, there are many in-built special functions that are very useful to do specific tasks.<br>
#     Here we will see few of the in-built functions that can be used to perform mathematical operations.
#     <iframe
#     src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=panda-syntax&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=import%2520%2520math%250A%250A%2523%2520--------------Number-theoretic%2520and%2520representation%2520functions--------------------------------------%250Along_string%2520%253D%2520%27%27%27%250Amath.ceil%28x%29%250AReturn%2520the%2520ceiling%2520of%2520x%252C%2520the%2520smallest%2520integer%2520greater%2520than%2520or%2520equal%2520to%2520x.%250AIf%2520x%2520is%2520not%2520a%2520float%252C%2520delegates%2520to%2520x.__ceil__%28%29%252C%2520which%2520should%2520return%2520an%2520Integral%2520value.%250A%27%27%27%250Aprint%28long_string%29%250Aprint%28%2522%255Cn--------------------math.ceil%28x%29-------------------------------%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404%2520---%2520%257Bmath.ceil%28404%29%257D%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404.01%2520---%2520%257Bmath.ceil%28404.01%29%257D%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404.36%2520---%2520%257Bmath.ceil%28404.36%29%257D%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404.50%2520---%2520%257Bmath.ceil%28404.50%29%257D%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404.86%2520---%2520%257Bmath.ceil%28404.86%29%257D%2522%29%250Aprint%28%2522---------------------------------------------------------------%255Cn%2522%29%250A%250Along_string%2520%253D%2520%27%27%27%250Amath.comb%28n%252C%2520k%29%250AReturn%2520the%2520number%2520of%2520ways%2520to%2520choose%2520k%2520items%2520from%2520n%2520items%2520without%2520repetition%2520and%2520without%2520order.%250AEvaluates%2520to%2520n%21%2520%252F%2520%28k%21%2520*%2520%28n%2520-%2520k%29%21%29%2520when%2520k%2520%253C%253D%2520n%2520and%2520evaluates%2520to%2520zero%2520when%2520k%2520%253E%2520n.%250AAlso%2520called%2520the%2520binomial%2520coefficient%2520because%2520it%2520is%2520equivalent%2520to%2520the%2520coefficient%2520of%2520k-th%2520term%2520in%2520polynomial%2520expansion%2520of%2520the%2520expression%2520%281%2520%252B%2520x%29%2520**%2520n.%250ARaises%2520TypeError%2520if%2520either%2520of%2520the%2520arguments%2520are%2520not%2520integers.%2520Raises%2520ValueError%2520if%2520either%2520of%2520the%2520arguments%2520are%2520negative.%250A%27%27%27%250Aprint%28long_string%29%250A%250Aprint%28%2522%255Cn-------------------math.comb%28n%252C%2520k%29-----------------------------%2522%29%250Aprint%28f%2522math.comb%28n%252C%2520k%29%2520---%2520for%2520number%2520%253D%2520404%252C%252010%2520---%2520%257Bmath.comb%28404%252C%252010%29%257D%2522%29%250Aprint%28f%2522math.comb%28n%252C%2520k%29%2520---%2520for%2520number%2520%253D%252010%252C%25202%2520---%2520%257Bmath.comb%2810%252C%25202%29%257D%2522%29%250Aprint%28f%2522math.comb%28n%252C%2520k%29%2520---%2520for%2520number%2520%253D%252010%252C%25201%2520---%2520%257Bmath.comb%2810%252C%25201%29%257D%2522%29%250Aprint%28f%2522math.comb%28n%252C%2520k%29%2520---%2520for%2520number%2520%253D%252010%252C%252010%2520---%2520%257Bmath.comb%2810%252C%252010%29%257D%2522%29%250Aprint%28f%2522math.comb%28n%252C%2520k%29%2520---%2520for%2520number%2520%253D%252010%252C%252011%2520---%2520%257Bmath.comb%2810%252C%252011%29%257D%2522%29%250A%2523%2520print%28f%2522math.comb%28n%252C%2520k%29%2520---%2520for%2520number%2520%253D%2520404.01%2520---%2520%257Bmath.comb%28404.01%252C%252010%29%257D%2522%29%2520%2523TypeError%253A%2520%27float%27%2520object%2520cannot%2520be%2520interpreted%2520as%2520an%2520integer%250A%2523print%28f%2522math.comb%28n%252C%2520k%29%2520---%2520for%2520number%2520%253D%2520-404%2520---%2520%257Bmath.comb%28-404%252C%252010%29%257D%2522%29%2520%2523ValueError%253A%2520n%2520must%2520be%2520a%2520non-negative%2520integer%250A%250Aprint%28%2522---------------------------------------------------------------%255Cn%2522%29%250A"
#     style="width: 810px; height: 469px; border:0; transform: scale(1); overflow:hidden;"
#     sandbox="allow-scripts allow-same-origin">
#     </iframe>
#     """, unsafe_allow_html=True)
#     github_gist("https://gist.github.com/ineelhere/c6b77aa48d3695c32712b18801adc43a", width=800, height=500)
#     codearea()

# def strings():
#     st.subheader("**Strings in python**")
#     st.markdown("""
#     Here we will see how to handle strings in python.  \n
#     When we deal with data, we mostly deal with strings - which we then reformat according to our choices.  \n
#     So, it is important that we deal properly with the strings such that we don't loose data.
#     <iframe
#     src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=panda-syntax&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=%2523%2520write%2520a%2520long%2520string%2520%28multiple%2520lines%2520without%2520using%2520%255Cn%29%250Along_string%2520%253D%2520%27%27%27%250AHello%2520there%21%250AWe%2520are%2520currently%2520creating%2520a%2520long%2520string.%250AWrite%2520multiple%2520lines%2520here%252C%250Awithout%2520any%2520worries.%2520B-%29%250A%27%27%27%250Aprint%28long_string%29%250A%250A%2523using%2520escape%2520sequences%250A%250A%2520%2520%2520%2520%2523it%27s%2520difficult%2520to%2520insert%2520a%2520special%2520character%2520in%2520a%2520string%2520or%2520print%2520statement.%250A%2520%2520%2520%2520%2523so%252C%2520we%2520use%2520%255C%2520as%2520our%2520saviour%21%250Aprint%28%2522See%252C%2520we%2520are%2520writing%2520%255C%2522%2520in%2520%2520a%2520print%2520statement%2520without%2520any%2520worries%21%2522%29%250Aprint%28%27Isn%255C%27t%2520it%2520awesome%253F%253F%27%29%250A%250A%2523newline%250Aprint%28%2522This%2520is%2520the%2520first%2520line%2520%255CnThis%2520is%2520the%2520second%2520line%2522%29%250A%250A%2523backspace%250Aprint%28%2522This%2520is%2520an%2520incomplete%2520li%255Cbne%2522%29%250A%250A%2523horizontal%2520tab%250Aprint%28%2522Here%2520comes%2520the%2520tab%255CtGot%2520that%253F%253F%2522%29%250A%250A%2523print%2520a%2520backslash%2520itself%250Aprint%28%2522So%252C%2520here%2520is%2520the%2520%255C%255C%2520you%2520wanted%2520to%2520see%21%2522%29%250A%250A%2523formating%2520a%2520string%2520%28we%2520have%2520already%2520seen%2520this%2520before%252C%2520now%2520it%2520is%2520time%2520to%2520realize%2520it%2520%21%21%29%250Aa%2520%253D%25202020%250Aprint%28%2522This%2520code%2520was%2520written%2520in%2520the%2520year%2520%2522%252Bstr%28a%29%29%2520%2523here%2520the%2520number%2520is%2520printed%2520in%2520form%2520of%2520a%2520string%2520otherwise%2520it%2520throws%2520an%2520error%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2523TypeError%253A%2520can%2520only%2520concatenate%2520str%2520%28not%2520%2522int%2522%29%2520to%2520str%250Aprint%28%2522After%252010%2520years%2520it%2520will%2520be%2520the%2520year%2520%2522%252Bstr%28a%252B10%29%29%2520%2523same%2520explanation%2520as%2520above%250A%2523now%2520let%2520us%2520use%2520a%2520shortcut%250Aprint%28f%2522The%2520code%2520is%2520written%2520in%2520the%2520year%2520%257Ba%257D%2522%29%2520%2523see%252C%2520how%2520simple%2520it%2520is%2520to%2520format%2520a%2520string%21%21%250Aprint%28f%2522After%252010%2520years%2520it%2520will%2520be%2520the%2520year%2520%257Ba%252B10%257D%2522%29%250A%250A%2523how%2520to%2520get%2520a%2520string%2520index%250Atext%2520%253D%2520%2522Climate%2520change%2520is%2520real%21%2522%250Aprint%28text%29%250Aprint%28text%255B1%253A10%255D%29%2520%2523counting%2520starts%2520from%25200%250Aprint%28text%255B0%253A10%255D%29%2520%2523now%2520see%2520the%2520difference%250Aprint%28text%255B%253A10%255D%29%2520%2523prints%2520first%252010%2520elements%250Aprint%28text%255B%253A%253A%255D%29%2520%2523prints%2520Everything%250Aprint%28text%255B-1%255D%29%2520%2523first%2520element%2520starting%2520from%2520the%2520end%2520of%2520the%2520string%250Aprint%28text%255B-3%255D%29%2520%2523third%2520element%2520starting%2520from%2520the%2520end%2520of%2520the%2520string%250Aprint%28text%255B%253A%253A-1%255D%29%2520%2523prints%2520in%2520reverse%2520order%250A%250A%2523%2520there%2520are%2520many%2520more%2520things%2520to%2520know%2520about%2520strings.%2520%250A%2523%2520You%2520are%2520welcome%2520to%2520add%2520anything%2520relevant%2520you%2520wish%2520to%2520in%2520this%2520notebook%21%250A%2523%2520Please%2520collaborate%2520and%2520contribute%2520%253A%29"
#     style="width: 810px; height: 469px; border:0; transform: scale(1); overflow:hidden;"
#     sandbox="allow-scripts allow-same-origin">
#     </iframe>
#     """, unsafe_allow_html=True)
#     github_gist("https://gist.github.com/ineelhere/1a384259bf5f8c5510eaf1b0cd419c88", width=800, height=500)
#     codearea()

def all():
    st.subheader("**Let's code!**")
    st.markdown("""
    * Open a notebook in Google Colab - <a href="https://colab.research.google.com/" target="_blank"><img width="64" height="64" src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="Github" > </a>
    * Follow along with the lines of codes listed below.
    * Simply copy pasting is not recommended, but if you are here for a quick revision, please feel free to do whatever that saves your time!
    * This whole notebook is [availabele here](https://github.com/ineelhere/pylearn/blob/master/codekitchen/ipynb_files/all_codes_py101.ipynb).


    
    """, unsafe_allow_html=True)
    github_gist('https://gist.github.com/ineelhere/16af99c0506f149f195ff0f3901577d1', width=800, height=500)
    st.write('![](https://imgs.xkcd.com/comics/python.png)')
    codearea()
    
