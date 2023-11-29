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
    "- Por ahora solo se soporta Mazda 3 motorizacion 122 CV BP 2023"
}

st.set_page_config(layout="wide")

df = pd.read_csv('rev_list_mazda3.txt',sep=";")
st.title('Comparador de precios revisiones Mazda España')


modelo = st.sidebar.selectbox('Modelo Coche:', ["Mazda 3"])

provincias = pd.unique(df['Provincia'])
provincias = np.append("Todas",provincias)
provincia_elegida = st.sidebar.selectbox('Provincia:', provincias)
if provincia_elegida != "Todas":
    print(provincia_elegida)
    df = df.iloc[0:][df["Provincia"] == provincia_elegida]

numeroRevision = pd.unique(df['Revision'])
numeroRevision = np.append("Todas",numeroRevision)
numeroRevision_elegida = st.sidebar.selectbox('Numero de revision:', numeroRevision)
print(df)
if numeroRevision_elegida != "Todas":
    df = df.iloc[0:][df["Revision"] == int(numeroRevision_elegida)]
    print(df)

motores = pd.unique(df['Motor'])
motores = np.append("Todos",motores)
motor_elegida = st.sidebar.selectbox('Motor:', motores)
if motor_elegida != "Todos":
    df = df.iloc[0:][df["Motor"] == motor_elegida]

if motor_elegida != "Todos" or provincia_elegida != "Todas" or numeroRevision_elegida != "Todas":
    height = int(35.2*(len(df.index)+1))
    st.dataframe(df.set_index(df.columns[0]),width=2000,height=height)
else:
    st.dataframe(df.set_index(df.columns[0]),width=2000)


# --- Projects & Accomplishments ---
st.write('\n')
st.write("---")
st.subheader("Changelog")
for project in CHANGELOG:
    st.write(f"{project}")

# --- Projects & Accomplishments ---
st.write('\n')
st.write("---")
st.subheader("About Me")
for project in ABOUT_ME:
    st.write(f"{project}")