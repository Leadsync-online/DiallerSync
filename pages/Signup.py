import streamlit as st
from supabase import create_client, Client
import Modules as md

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

col1, col2, col3 = st.columns(3)

with col2:
    st.image("images/Dialler_Sync.png",width = 180)
    st.write("Create a new account.")

# Sign-up page
def signup_page():

    col1, col2, col3 = st.columns([1,7,1])  # Adjust column ratios as needed
    with col2:
        signup_email = st.text_input("New Email", key="signup_email")
        signup_password = st.text_input("New Password", type="password", key="signup_password")
        
        if st.button("Create Account",use_container_width=True):
            md.signup(signup_email, signup_password)
        
            # Back to login button
        if st.button("Back to Login",use_container_width=True):
            st.switch_page("Login.py")

signup_page()
