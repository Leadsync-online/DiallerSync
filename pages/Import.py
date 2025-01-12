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

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
