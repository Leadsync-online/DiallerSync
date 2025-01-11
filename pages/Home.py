import streamlit as st
from supabase import create_client, Client
import Modules as md
from datetime import date, timedelta

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

st.header("Dashboard")

with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.selectbox(
        "Please select campaign?",
        ("Onair", "MTN", "Mobile phone"))
    
    with col2:
        st.date_input("Please select date?", today)
    
    with col3:
        st.text("")
        if st.button("Import file", use_container_width=True):
            st.switch_page("pages/Import.py")

st.subheader("Dialler Statistics", divider=False)
