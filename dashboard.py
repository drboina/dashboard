import streamlit as st
import pandas as pd
import numpy as np
import openpyxl

st.image("logowhite.png")
st.title("Sistema de Reportes del Ejecutivo del Estado")
st.sidebar.image("image.png")

option = st.sidebar.selectbox("Opciones",('Licitaciones y Contratos','Presupuesto','Ordenes de pago','Minutario','Adquisiciones'))

st.header(option)

if option == 'Licitaciones y Contratos':
    st.markdown ('___________________________________________________')

    st.subheader("Reporte de Contratos 2024")
    
    df=pd.read_excel("CONTRATOS_2023.xlsx")
    df_proc=df.groupby(["TIPO CONTRATO"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    
    st.dataframe(df_proc)

    





if option == 'Presupuesto':
    st.subheader("Presupuesto de Egresos 2024")
    
    df=pd.read_excel("TECHO PPTAL 2024 EJECUTIVO.xlsx")
     
    st.dataframe(df)
     
if option == 'Ordenes de pago':
    st.subheader("Status de Ordenes de pago")

if option == 'Minutario':
    st.subheader("Control de Oficios de la Coordinación Ejecutiva de Administración y Finanzas")

if option == 'Adquisiciones':
    st.subheader("Reporte de Adquisiciones 2024")





