import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from colorspacious import cspace_converter # type: ignore
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

cmaps = {}

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

def plot_color_gradients(category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} colormaps', fontsize=14)

    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=mpl.colormaps[name])
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    # Save colormap list for later.
    cmaps[category] = cmap_list


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
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                 shadow=True)
        ax1.axis('equal')
        st.pyplot(fig1)
        plt.show()
    
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





