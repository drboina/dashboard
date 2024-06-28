import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
import plotly.graph_objs as go
theme_plotly = None 


st.set_page_config(page_title="Reportes",page_icon="🌍",layout="wide")
st.header("Sistema de Reportes del Ejecutivo")
st.sidebar.image("logo.png")


# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


option = st.sidebar.selectbox("Opciones",('Licitaciones y Contratos','Presupuesto','Ordenes de pago','Minutario','Adquisiciones'))

st.header(option)

if option == 'Licitaciones y Contratos':
    st.markdown ('___________________________________________________')

    st.subheader("Reporte de Contratos 2023")
    df=pd.read_excel("CONTRATOS_2023.xlsx", dtype={'PARTIDA' : str, 'CENTRO GESTOR' : str, 'MONTO TOTAL ADJUDICADO': float})  
 
    no_contratos = len(pd.Series(df['CONTRATO']).value_counts())
    monto_total=float(pd.Series(df["MONTO TOTAL ADJUDICADO"].sum()))
    
    total1,total2 = st.columns(2,gap='small')
    
    with total2:
        st.info('Monto total adjudicado:',icon="💰")
        st.metric(label="",value=f"{monto_total:,.0f}")

    with total1:
        st.info('No. Contratos')
        st.metric(label="",value=f"{no_contratos:,.0f}")

    st.markdown ('___________________________________________________')
    
    df_proc=df.groupby(["TIPO CONTRATO"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    df_proV=df.groupby(["PROVEEDOR"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    df_partida=df.groupby(["PARTIDA"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    df_ua=df.groupby(["UNIDAD"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    
    side1,side2 = st.columns(2,gap='small')
  
    with side1:
        st.subheader("Procedimientos de Contratación 2023")
        st.dataframe(df_proc)

    with side2:
        labels = df_proc.index
        sizes = df_proc.values
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=False)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)
    
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





