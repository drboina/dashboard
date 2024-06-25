import streamlit as st
import pandas as pd
import numpy as np
import openpyxl

st.title("Sistema de Reportes del Ejecutivo")
st.sidebar.image("coord.png")

option = st.sidebar.selectbox("Opciones",('Licitaciones y Contratos','Presupuesto','Ordenes de pago','Minutario','Adquisiciones'))

st.header(option)

if option == 'Licitaciones y Contratos':
    st.markdown ('___________________________________________________')

    st.subheader("Reporte de Contratos 2024")
    
    df=pd.read_excel("CONTRATOS_2023.xlsx")

    df_proc=df.groupby(["TIPO CONTRATO"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    df_proV=df.groupby(["PROVEEDOR"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    df_partida=df.groupby(["PARTIDA"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    df_ua=df.groupby(["UNIDAD"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)

    st.dataframe(df)

    st.markdown ('___________________________________________________')
    st.subheader("Procedimientos de Contrataciòn 2024")
    st.dataframe(df_proc)

    st.markdown ('___________________________________________________')
    st.subheader("Proveedores de Contratos 2024")
    st.dataframe(df_proV)

    st.markdown ('___________________________________________________')
    st.subheader("Partidas del Gasto de Contratos 2024")
    st.dataframe(df_partida)
    
    st.markdown ('___________________________________________________')
    st.subheader("Unidades Administrativas Contratos 2024")
    st.dataframe(df_ua)
    
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





