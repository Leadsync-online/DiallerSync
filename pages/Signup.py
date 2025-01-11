import streamlit as st
from supabase import create_client, Client

# Sign-up page
def signup_page():
    st.title("Sign Up")
    st.write("Create a new account.")

    signup_email = st.text_input("New Email", key="signup_email")
    signup_password = st.text_input("New Password", type="password", key="signup_password")
    if st.button("Create Account"):
        signup(signup_email, signup_password)

    # Back to login button
    if st.button("Back to Login"):
        st.switch_page("Login")
