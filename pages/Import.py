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

st.header("Import new file")

uploaded_file = st.file_uploader("Upload a CSV, TXT, or Excel file", type=["csv", "txt", "xls", "xlsx"])

if uploaded_file is not None:
    try:
        df = md.read_file(uploaded_file)
        st.write("File successfully read. Here are the first few rows:")
        st.dataframe(df.head())

        md.select_and_map_fields(df)
    except Exception as e:
        st.error(f"Error: {e}")

    

