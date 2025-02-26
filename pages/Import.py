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

uploaded_files = st.file_uploader("Select your file", accept_multiple_files=True, type=["csv", "txt", "xls", "xlsx"])

if uploaded_file is not None:
    try:
        file_path = uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        df = md.read_file(file_path)
        st.write("File successfully read. Here are the first few rows:")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error: {e}")
