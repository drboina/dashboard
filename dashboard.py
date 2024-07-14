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
    df_techo=pd.read_excel("techo_pptal_2023.xlsx", dtype={'PARTIDA' : str, 'CAPITULO' : str, 'CENTRO GESTOR' : str, 'TOTAL': float}) 
    no_contratos = len(pd.Series(df['CONTRATO']).value_counts())
    monto_total=float(pd.Series(df["MONTO TOTAL ADJUDICADO"].sum()))
    no_proveedores = len(pd.Series(df['PROVEEDOR']).value_counts())
    techo = df_techo['TOTAL'].sum()
    
    total1,total2,total3,total4 = st.columns(4,gap='small')
    
    with total1:
        st.info('No. de Contratos adjudicados')
        st.metric(label="",value=f"{no_contratos:,.0f}")

    with total2:
        st.info('Monto total adjudicado:')
        st.metric(label="",value=f"${monto_total:,.0f} M.N.")
    
    with total3:
        st.info('Presupuesto Aprobado 2023:')
        st.metric(label="",value=f"${techo:,.0f} M.N.")

    with total4:
        st.info('% Presupuesto Comprometido:')
        porc_techo = monto_total/techo*100
        st.metric(label="",value=f"{porc_techo:,.2f}%")
    st.markdown ('___________________________________________________')
    
    df_proc=df.groupby(["TIPO CONTRATO"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)    
    st.subheader("Procedimientos de Contratación 2023")
   
    side1,side2 = st.columns(2,gap='large')
    with side1:
        st.dataframe(df_proc)

    with side2:
        labels = df_proc.index
        sizes = df_proc.values
        fig1 , ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels,  autopct='%1.1f%%', shadow=True)
        ax1.axis('equal')
        st.pyplot(fig1)
    
    st.markdown ('___________________________________________________')        
            
    st.subheader("Gasto por Partida de Contratos",)

    side1,side2 = st.columns(2,gap='small')
    with side1:
        df_partida=df.groupby(["PARTIDA"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
        partida = list(df_partida.index.astype(str))
        values = df_partida.to_list()
        fig, ax2 = plt.subplots()
        plt.bar(partida, values, color ='maroon',)
        plt.xlabel("Partida")
        plt.xticks(font='Arial', fontsize=7)
        plt.yticks(font='Arial', fontsize=7)
        ax2.set_xticklabels(partida, rotation=45, ha='right')

        st.pyplot(fig)
    
    with side2:
        st.dataframe(df_partida)

    st.markdown ('___________________________________________________')

    df_ua=df.groupby(["UNIDAD"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    st.subheader("Unidades Administrativas Contratos")
   
    side1,side2 = st.columns(2,gap='large')
    with side1:
        st.dataframe(df_ua)

    with side2:
        labels = df_ua.index
        sizes = df_ua.values
        fig3 , ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
        ax1.axis('equal')
        st.pyplot(fig3)

    st.markdown ('___________________________________________________')
    df_proV=df.groupby(["PROVEEDOR"])["MONTO TOTAL ADJUDICADO"].sum().astype(int).sort_values(ascending=False)
    st.subheader("Proveedores de Contratos")
    st.dataframe(df_proV)

    st.markdown ('___________________________________________________')
    
if option == 'Presupuesto':
    st.subheader("Estado del Ejercicio del Ejecutivo")
    
     
    st.dataframe(df)
     
if option == 'Ordenes de pago':
    st.subheader("Status de Ordenes de pago")

if option == 'Minutario':
    st.subheader("PAAAS")





