import streamlit as st
from supabase import create_client, Client
import Modules as md
import time

st.set_page_config(initial_sidebar_state="collapsed")

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

