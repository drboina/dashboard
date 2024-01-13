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
    
    st.dataframe(df)

    monto_LPA=df.loc[df ['TIPO CONTRATO'] == 'LPA', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_AD=df.loc[df ['TIPO CONTRATO'] == 'AD', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_LPC=df.loc[df ['TIPO CONTRATO'] == 'LPC', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_CM=df.loc[df ['TIPO CONTRATO'] == 'CM', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_LSA=df.loc[df ['TIPO CONTRATO'] == 'LSA', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_AR=df.loc[df ['TIPO CONTRATO'] == 'AR', 'MONTO TOTAL ADJUDICADO'].sum()
    sumatipo=[monto_LPA, monto_AD, monto_LPC, monto_CM, monto_LSA, monto_AR]
    monto_total=df["MONTO TOTAL ADJUDICADO"].sum()


    df_c=pd.DataFrame({"No. CONTRATOS":df["TIPO CONTRATO"].value_counts(), 
                       "MONTO TOTAL":sumatipo,
                       "%":sumatipo/monto_total*100}).astype(int)
    
    df_c = df_c.sort_values(by=['MONTO TOTAL'], ascending=False)
    st.dataframe(df_c)
    
    
    monto_CELGERP=df.loc[df ['UNIDAD'] == 'CELGERP', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_CEAyF=df.loc[df ['UNIDAD'] == 'CEAyF', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_CGSECS=df.loc[df ['UNIDAD'] == 'CGSECS', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_JOEE=df.loc[df ['UNIDAD'] == 'JOEE', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_SPART=df.loc[df ['UNIDAD'] == 'S. PARTICULAR', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_STMS=df.loc[df ['UNIDAD'] == 'STMS', 'MONTO TOTAL ADJUDICADO'].sum()
    monto_ATC=df.loc[df ['UNIDAD'] == 'ATTN CIUDADANA', 'MONTO TOTAL ADJUDICADO'].sum()
    suma=[monto_CELGERP, monto_CEAyF, monto_CGSECS, monto_JOEE,monto_SPART,monto_STMS,monto_ATC]

    df_UA=pd.DataFrame({"No. CONTRATOS":df["UNIDAD"].value_counts(), 
                       "MONTO TOTAL":suma, 
                       "%":suma/monto_total*100}).astype(int)
    
    df_UA = df_UA.sort_values(by=['MONTO TOTAL'], ascending=False)

    st.dataframe(df_UA)

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





