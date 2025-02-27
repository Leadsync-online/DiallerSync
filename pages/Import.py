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
    [data-testid="stSidebarCollapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    st.header("Import new file")

with col4:
    if st.button("Dashboard", use_container_width=True):
        st.switch_page("pages/Home.py")

uploaded_file = st.file_uploader("", type=["csv", "txt", "xls", "xlsx"])

if uploaded_file is not None:
    try:
        df = md.read_file(uploaded_file)
        st.write("File successfully read. Here are the first few rows:")

        dipositiontable = md.get_table_columns("tm_dialler_disposition")
        
        with st.form("my_form"):
            md.map_fields_to_supabase(df,dipositiontable)

    except Exception as e:
        st.error(f"Error: {e}")

    

