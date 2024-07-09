#import library yang dibutuhkan

import streamlit as st
from web_functions import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

#Membuat sidebar
st.sidebar.title("Navigasi")

#Membuat radio option
page = st.sidebar.radio("Page", list(Tabs.keys()))

#load dataset
df, x, y = load_data()

#kondisi call app function
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, x,y)
else:
    Tabs[page].app()