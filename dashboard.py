import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Reportes Ejecutivo", layout="wide")
st.header("Sistema de Reportes del Ejecutivo")
st.sidebar.image("logo.png")

option = st.sidebar.selectbox("Opciones",('Licitaciones y Contratos','Presupuesto','Ordenes de pago','PAAAS'))

st.header(option)

if option == 'Licitaciones y Contratos':
    st.markdown ('___________________________________________________')

    st.subheader("Reporte de Contratos 2023")
    df=pd.read_excel("CONTRATOS_2023.xlsx", dtype={'PARTIDA' : str, 'CENTRO GESTOR' : str, 'MONTO TOTAL ADJUDICADO': float})  

    no_contratos = len(pd.Series(df['CONTRATO']).value_counts())
    monto_total=float(pd.Series(df["MONTO TOTAL ADJUDICADO"].sum()))
    
    total1,total2 = st.columns(2,gap='small')
    
    with total1:
        st.info('No. Contratos')
        st.metric(label="",value=f"{no_contratos:,.0f}")

    with total2:
        st.info('Monto total adjudicado:')
        st.metric(label="",value=f"${monto_total:,.0f} M.N.")

    st.markdown ('___________________________________________________')
    
    df_proc=df.groupby(["TIPO CONTRATO"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)    
    st.subheader("Procedimientos de Contratación 2023")
    side1,side2 = st.columns(2,gap='small')
  
    with side1:
        st.text('Tabla 1. Monto total por procedimiento')
        st.dataframe(df_proc)

    with side2:
        labels = df_proc.index
        sizes = df_proc.values
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
        ax1.axis('equal')
        st.pyplot(fig1)
        plt.show()
        st.text('Figura 1. Porcentaje por tipo de procedimiento')
    
    st.markdown ('___________________________________________________')
    df_proV=df.groupby(["PROVEEDOR"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    st.subheader("Proveedores de Contratos 2023")
    st.dataframe(df_proV)

    st.markdown ('___________________________________________________')
    df_partida=df.groupby(["PARTIDA"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    st.subheader("Gasto por Partida de Contratos 2023")
    st.dataframe(df_partida)
    
    st.markdown ('___________________________________________________')
    df_ua=df.groupby(["UNIDAD"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    st.subheader("Unidades Administrativas Contratos 2023")
    st.dataframe(df_ua)
    
if option == 'Presupuesto':
    st.subheader("Estado del Ejercicio del Ejecutivo")
    
    df=pd.read_excel("TECHO PPTAL 2024 EJECUTIVO.xlsx")
     
    st.dataframe(df)
     
if option == 'Ordenes de pago':
    st.subheader("Status de Ordenes de pago")

if option == 'Minutario':
    st.subheader("PAAAS")





