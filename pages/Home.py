import streamlit as st
from supabase import create_client, Client
import Modules as md

st.set_page_config(initial_sidebar_state="collapsed")

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

st.header("Dashboard")
