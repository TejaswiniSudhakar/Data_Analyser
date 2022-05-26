import streamlit as st
from DV_apps import Home
from DV_apps import Visualization
from DV_apps import Dashboard
from DV_apps import Query
from PIL import Image

st.set_page_config(layout="wide")
s = st.button("Home")
PAGES = {
    "Home": Home,
    "Visualizer": Visualization,
    "Dashboard": Dashboard,
    "Query Solver": Query
}

st.image("Learn Leadspace 4_0.png")
if s == True:
    selection = st.selectbox("Choose one", list(PAGES.keys()), key ='2')
    Home.app()
else:
    selection = st.selectbox("Choose one", list(PAGES.keys()), key ='3')
    page = PAGES[selection]
    page.app()
