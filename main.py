import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import streamlit as st
import numpy as np

ABOUT_ME = {
    "Si te gusta lo que hago puedes seguirme en :",
    "- 𝕏 Mi cuenta de [X](https://twitter.com/R00tedSec)",
    "- 🧑‍💻Mi [Github](https://github.com/R00tedSec)"
}
CHANGELOG = {
    "Version 1.0.0:",
    "- Primera version del comparador de precios",
    "- Por ahora solo se soporta Mazda 3 BP 2023"
}


st.set_page_config(
    page_title="Comparador Presupuestos Mazda",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.calculaturevisionmazda.com/',
        'Report a bug': "https://twitter.com/R00tedSec",
        'About': "#  Compara los presupuestos de tus revisiones en Mazda"
    }
    )


df = pd.read_csv('rev_list_mazda3.txt',sep=";")
st.title('Comparador de precios revisiones Mazda España')


modelo = st.sidebar.selectbox('Modelo Coche:', ["Mazda 3"])

provincias = pd.unique(df['Provincia'])
provincias = np.append("Todas",provincias)
provincia_elegida = st.sidebar.selectbox('Provincia:', provincias)
if provincia_elegida != "Todas":
    df = df.iloc[0:][df["Provincia"] == provincia_elegida]

numeroRevision = pd.unique(df['Revision'])
numeroRevision = np.append("Todas",numeroRevision)
numeroRevision_elegida = st.sidebar.selectbox('Numero de revision:', numeroRevision)
if numeroRevision_elegida != "Todas":
    df = df.iloc[0:][df["Revision"] == int(numeroRevision_elegida)]

motores = pd.unique(df['Motor'])
motores = np.append("Todos",motores)
motor_elegida = st.sidebar.selectbox('Motor:', motores)
if motor_elegida != "Todos":
    df = df.iloc[0:][df["Motor"] == motor_elegida]

print(f'Filtro aplicado:{provincia_elegida} {numeroRevision_elegida} {motor_elegida}')
if motor_elegida != "Todos" or provincia_elegida != "Todas" or numeroRevision_elegida != "Todas":
    height = int(35.2*(len(df.index)+1))
    st.dataframe(df.set_index(df.columns[0]),width=2000,height=height)
else:
    st.dataframe(df.set_index(df.columns[0]),width=2000)


# --- Projects & Accomplishments ---
st.write('\n')
st.write("---")
st.subheader("⚠️ Disclamer ⚠️")
st.write(f"⚠️ El precio que aqui aparece ha sido extraido de la web oficial de mazda, estos precios pueden no ser los definitivos o no estar actualizados. ⚠️")
st.write(f"⚠️ Usa esta web como orientacion, no como web de consulta oficial ⚠️")
st.write(f'Muchas gracias por hacer uso de la herramienta ❤️')

# --- Projects & Accomplishments ---
st.write('\n')
st.write("---")
st.subheader("🗒️Changelog🗒️")
for project in CHANGELOG:
    st.write(f"{project}")

# --- Projects & Accomplishments ---
st.write('\n')
st.write("---")
st.subheader("🧑‍💻 About Me 🧑‍💻")
for project in ABOUT_ME:
    st.write(f"{project}")