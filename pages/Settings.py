import streamlit as st
from supabase import create_client, Client
import Modules as md
from datetime import date, timedelta
import pandas as pd
import numpy as np

today = date.today()

st.set_page_config(initial_sidebar_state="collapsed",layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"]{
        visibility: hidden;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

col1, col2 = st.columns([1,1])

with col1:
    st.header("Settings")
