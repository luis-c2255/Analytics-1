import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px 
import plotly.graph_objects as go 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.preprocessing import StandardScaler 
import pickle

from utils.theme import Components, Colors, apply_chart_theme, init_page

init_page("Customer Churn Analytics Dashboard", "🏦")

# Load custom CSS
try:
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Custom CSS file not found. Using default styling.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Churn_Modelling.csv')
    df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1) 
    return df