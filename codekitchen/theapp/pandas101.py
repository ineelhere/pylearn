import streamlit as st
from streamlit_embedcode import github_gist
import pandas as pd

def pandas101():
    st.header("**`pandas101` - Learn data analysis and manipulation **")

    st.markdown ('''
    **[pandas](https://pandas.pydata.org/)** is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
    built on top of the Python programming language.

    This section of `dspy` is all about geting started with pandas. We will be using a `code-first` approach to encourage application based learning. 

    Keep following us as we proceed. Please log in to [Google Colab](https://colab.research.google.com/) to write codes and experiment with your data.
    ''')

    st.subheader("**1. Import the module first**")
    st.markdown('''
    * [Install pandas](https://pandas.pydata.org/docs/getting_started/index.html) into your environment first (not needed if you are on Google Colab)
    * Pandas is basically a python library/module, and like any python module, we need to first import them into our code
    * Here's is how it's done

    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=import%2520pandas%2520as%2520pd"
    style="width: 242px; height: 133px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>

    * Note: It's not mandatory to call it `pd`. You may call it whatever you wish. Developers like to abbreviate it as `pd` so that communicating with code gets easier globally.
    
    ![](https://pics.me.me/import-numpy-as-pd-import-pandas-as-np-df-np-56635981.png)
    ''', unsafe_allow_html= True)

    st.subheader("**2. Series vs DataFrame**")
    st.markdown('''
    * A pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) and [pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) dataframe are 2 different data-types.
    * Dataframe is two-dimensional whereas, series is one-dimensional.
    * Copy these snippets on 2 different cells of your jupyter notebook or google colab and notice the differences -

    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=%2523working%2520with%2520series%250Aseries%2520%253D%2520pd.Series%28%255B%27abcd%27%252C%2520%27efgh%27%252C%2520%27ijklmnop%27%255D%29%2520%2523%2520S%2520is%2520capital%250Aseries"
    style="width: 621px; height: 175px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>

    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=%250A%2523working%2520with%2520series%250Aseries%2520%253D%2520pd.Series%28%255B%27abcd%27%252C%2520%27efgh%27%252C%2520%27ijklmnop%27%255D%29%2520%2523%2520S%2520is%2520capital%250A%250A%2523working%2520with%2520dataframes%250Adf%2520%253D%2520pd.DataFrame%28%257B%2522column1%2522%253A%2520series%252C%2520%2522column2%2522%253A%2520series%257D%29%250Adf%250A%250A%2523used%2520the%2520series%2520to%2520create%2520a%2520dataframe"
    style="width: 621px; height: 301px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>

    * Interesting! Isn't it?

    ''', unsafe_allow_html= True)
    github_gist('https://gist.github.com/ineelhere/5814fb6f29c42081945f1f31c7c09aa2', width=800)

    st.subheader("**3. Export your dataframe**")

    st.markdown("""
    ### Prelude
    * Pandas basically reads your data at source and stores it into a dataframe - the two dimensional data format we spoke above.
    * Your data at the source can be in various formats, like - `csv`, `xlsx`, `tsv`, `json` etc.
    * For every data format pandas has a solution. Not everything can be covered here, so we highly encourage you to google these things!
    
    ### Talking about exporting the dataframe
    * `to_csv` command helps to export the dataframe into csv file.
    * More info can be found here [pandas.DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
    * Similarly, you can also export files in xlsx format. [Click here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas-dataframe-to-excel)
    * It is encouraged that you explore the original documentation for more file formats.

    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=import%2520pandas%2520as%2520pd%250A%2523creating%2520the%2520dataframe%250Aseries%2520%253D%2520pd.Series%28%255B%27abcd%27%252C%2520%27efgh%27%252C%2520%27ijklmnop%27%252C%2520%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%27abcd%27%252C%2520%27efgh%27%252C%2520%27ijklmnop%27%252C%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%27abcd%27%252C%2520%27efgh%27%252C%2520%27ijklmnop%27%255D%29%2520%2523%2520S%2520is%2520capital%250Adf%2520%253D%2520pd.DataFrame%28%257B%2522column1%2522%253A%2520series%252C%2520%2522column2%2522%253A%2520series%257D%29%250A%2523write%2520this%2520dataframe%2520into%2520a%2520csv%2520file%250Adf.to_csv%28%2522example_file.csv%2522%252C%2520index%253DFalse%29%2520%250A%2523index%253DFalse%2520helps%2520to%2520avoid%2520creating%2520an%2520index%2520in%2520a%2520saved%2520csv"
    style="width: 621px; height: 301px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>

    The `example_file.csv` file created as a result of the above code is available [here](https://github.com/ineelhere/pylearn/blob/master/codekitchen/datafiles/example_file.csv)
 
    """, unsafe_allow_html=True)
    github_gist('https://gist.github.com/ineelhere/8c9b5e191328bad9be9182704b3f49da', width=800)
