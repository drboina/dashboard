import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Reportes Ejecutivo", layout="wide")
st.header("Sistema de Reportes del Ejecutivo")
st.sidebar.image("coord.png")

option = st.sidebar.selectbox("Opciones",('Licitaciones y Contratos','Presupuesto','Ordenes de pago','PAAAS'))

st.header(option)

if option == 'Licitaciones y Contratos':
    st.markdown ('___________________________________________________')

    st.subheader("Reporte de Contratos 2023")
    df=pd.read_excel("CONTRATOS_2023.xlsx", dtype={'PARTIDA' : str, 'CENTRO GESTOR' : str, 'MONTO TOTAL ADJUDICADO': float})  

    no_contratos = len(pd.Series(df['CONTRATO']).value_counts())
    monto_total=float(pd.Series(df["MONTO TOTAL ADJUDICADO"].sum()))
    no_proveedores = len(pd.Series(df['PROVEEDOR']).value_counts())
    
    total1,total2,tatal3 = st.columns(3,gap='medium')
    
    with total2:
        st.info('No. de Contratos adjudicados')
        st.metric(label="",value=f"{no_contratos:,.0f}")

    with total1:
        st.info('Monto total adjudicado:')
        st.metric(label="",value=f"${monto_total:,.0f} M.N.")
    
    with tatal3:
        st.info('No. de Proveedores:')
        st.metric(label="",value=f"{no_proveedores:,.0f}")

    st.markdown ('___________________________________________________')
    
    df_proc=df.groupby(["TIPO CONTRATO"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)    
    st.subheader("Procedimientos de Contratación 2023")
    side1,side2 = st.columns(2,gap='small')
  
    with side1:
        st.dataframe(df_proc)

    with side2:
        labels = df_proc.index
        sizes = df_proc.values
        colors = ['#90060c','#90060c','#99ff99','#e58725','#90060c']
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
        ax1.axis('equal')
        st.pyplot(fig1)
        st.text('Figura 1. Porcentaje por tipo de procedimiento')
    
    st.markdown ('___________________________________________________')
    st.subheader("Gasto por Partida de Contratos 2023",)
    col1,col2 = st.columns(2,gap="medium")
    df_partida=df.groupby(["PARTIDA"])["MONTO TOTAL ADJUDICADO"].sum().sort_values(ascending=False)

    with col2:
        st.table(df_partida)

    with col1:
        df_partida=df.groupby(["PARTIDA"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=True)
        partida = list(df_partida.index.astype(str))
        values = df_partida.to_list()

        fig = plt.figure(figsize = (10, 24))
        plt.barh(partida, values, color ='maroon',)
        plt.xlabel("Monto adjudicada [M.N]",fontsize=20)
        plt.yticks(fontsize=20)
        plt.xticks(fontsize=18)
        st.pyplot(fig)
    
    st.markdown ('___________________________________________________')
    df_ua=df.groupby(["UNIDAD"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    st.subheader("Unidades Administrativas Contratos 2023")
    st.dataframe(df_ua)

    st.markdown ('___________________________________________________')
    df_proV=df.groupby(["PROVEEDOR"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    st.subheader("Proveedores de Contratos 2023")
    st.dataframe(df_proV)

    st.markdown ('___________________________________________________')
    
if option == 'Presupuesto':
    st.subheader("Estado del Ejercicio del Ejecutivo")
    
    df=pd.read_excel("TECHO PPTAL 2024 EJECUTIVO.xlsx")
     
    st.dataframe(df)
     
if option == 'Ordenes de pago':
    st.subheader("Status de Ordenes de pago")

if option == 'Minutario':
    st.subheader("PAAAS")





