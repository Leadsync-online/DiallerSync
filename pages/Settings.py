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

    if st.button("Account Settings", use_container_width=True):
        with col2:
            st.write("yesty")

    if st.button("Dashboard", use_container_width=True):
        st.switch_page("pages/Home.py")
    
    if st.button("Logout", use_container_width=True):
        st.switch_page("Login.py")
