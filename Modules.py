import streamlit as st
from supabase import create_client, Client

def login(username, password):
    try:
        user = supabase.auth.sign_in_with_password({"email": username, "password": password})
        return user
    except Exception:
        st.error("Login failed. Check your username and password.")
        return None

# Define login and signup functions

def signup(username, password):
    try:
        user = supabase.auth.sign_up({"email": username, "password": password})
        st.success("Sign-up successful! You can now log in.")
        st.switch_page("Login")
    except Exception as e:
        st.error(f"Sign-up failed: {e}")
