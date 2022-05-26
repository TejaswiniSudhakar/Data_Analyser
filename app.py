import streamlit as st
import Home
import Visualization
import Dashboard
import Query
import pandas as pd
import numpy as np
import plotly_express as px
import matplotlib.pyplot as plt

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
