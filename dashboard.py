import streamlit as st
import pandas as pd
import numpy as np
import openpyxl


st.image("logowhite.png")

st.title("Sistema de Reportes")

st.header("Ejecutivo del Estado")

st.sidebar.image("image.png")

st.sidebar.title("Reportes")

option = st.sidebar.selectbox("Opciones",('Contratos','Presupuesto','Ordenes de pago','Minutario','Adquisiciones'))

st.header(option)

if option == 'Contratos':
    st.subheader("Reporte de Contratos 2024")
    
    df=pd.read_excel("CONTRATOS 2023.xlsx")
    
    monto_LPA=df. loc [df ['TIPO CONTRATO'] == 'LPA', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_AD=df. loc [df ['TIPO CONTRATO'] == 'AD', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_LPC=df. loc [df ['TIPO CONTRATO'] == 'LPC', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_CM=df. loc [df ['TIPO CONTRATO'] == 'CM', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_LSA=df. loc [df ['TIPO CONTRATO'] == 'LSA', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_AR=df. loc [df ['TIPO CONTRATO'] == 'AR', 'MONTO TOTAL ADJUDICADO'].sum()
    sumatipo=[monto_LPA, monto_AD, monto_LPC, monto_CM, monto_LSA, monto_AR]
    
    df_c=pd.DataFrame({"CANTIDAD":df["TIPO CONTRATO"].value_counts(), 
                       "MONTO TOTAL":sumatipo}).astype(int)
    df_c = df_c.sort_values(by=['MONTO TOTAL'], ascending=False)
    st.dataframe(df_c)
    

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





