import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import streamlit as st

ABOUT_ME = {
    "Si te gusta lo que hago puedes seguirme en :",
    "- 𝕏 Mi cuenta de [X](https://twitter.com/R00tedSec)",
    "- 🧑‍💻Mi [Github](https://github.com/R00tedSec)"
}
CHANGELOG = {
    "##### Version 1.0.0:  ",
    "- Primera version del comparador de precios",
    "- Por ahora solo se soporta Mazda 3 (122,150,186 CV Manual/Automatico)"
}

st.set_page_config(layout="wide")

df = pd.read_csv('rev_list_mazda3.txt',sep=";")
st.title('Comparador de precios revisiones Mazda España')


numeroRevision_elegida = st.sidebar.selectbox('Modelo Coche:', ["Mazda 3"])

provincias = df['Provincia'].drop_duplicates()
provincia_elegida = st.sidebar.selectbox('Provincia:', provincias)
df = df.iloc[0:][df["Provincia"] == provincia_elegida]

numeroRevision = df['Revision'].drop_duplicates()
numeroRevision_elegida = st.sidebar.selectbox('Numero de revision:', numeroRevision)
df = df.iloc[0:][df["Revision"] == numeroRevision_elegida]


motores = df['Motor'].drop_duplicates()
motor_elegida = st.sidebar.selectbox('Motor:', motores)
df = df.iloc[0:][df["Motor"] == motor_elegida]

Transmision = df['Transmision'].drop_duplicates()
Transmision_elegida = st.sidebar.selectbox('Transmision:', Transmision)
df = df.iloc[0:][df["Transmision"] == Transmision_elegida]


print(df)

height = int(35.2*(len(df.index)+1))

st.dataframe(df.set_index(df.columns[0]),width=2000,height=height)


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
