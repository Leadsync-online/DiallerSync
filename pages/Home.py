import streamlit as st
from supabase import create_client, Client
import Modules as md

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

st.header("Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),)

    st.write("You selected:", option)
