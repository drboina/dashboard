import streamlit as st
import pandas as pd
import numpy as np


st.image("logo.png")

st.title("Sistema de Reportes")

st.header("Ejecutivo del Estado")

st.sidebar.image("coord.png")

st.sidebar.title("Reportes")

option = st.sidebar.selectbox("Opciones",('Contratos','Presupuesto','Ordenes de pago','Minutario','Adquisiciones'))

st.header(option)

if option == 'Contratos':
    st.subheader("Contratos dashboard 2024")
    

if option == 'Presupuesto':
    st.subheader("Ejercicio del Presupuesto de Egresos 2024")

if option == 'Ordenes de pago':
    st.subheader("Status de Ordenes de pago")

if option == 'Minutario':
    st.subheader("Control de Oficios de la Coordinación Ejecutiva de Administración y Finanzas")

if option == 'Adquisiciones':
    st.subheader("Reporte de Adquisiciones 2024")





