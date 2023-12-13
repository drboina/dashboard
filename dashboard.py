import streamlit as st
import pandas as pd
import numpy as np


st.image("LOGO.PNG")

st.title("Este es el foking title")

st.header("thas the header")

st.write("Este es el textp regular")

st.subheader("thas the header")

st.sidebar.title("Opciones")

df=pd.DataFrame(np.random.randn(30,20), columns=('col %d' % i for i in range(20)))

option = st.sidebar.selectbox("Que dashboard?", ('twitter','wallstreetbets','stocktwits','chart','pattern'))

st.header(option)

if option == 'twitter':
    st.subheader("twitter dashboard logic")
    st.dataframe(df)

if option == 'wallstreetbets':
    st.subheader("wallstreetbets dashboard biatch")

if option == 'stocktwits':
    st.subheader("stocktwits dashboard")

if option == 'chart':
    st.subheader("el chart dashboard")

if option == 'pattern':
    st.subheader("this pattern dashboard")





