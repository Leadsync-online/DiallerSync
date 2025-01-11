import streamlit as st
from supabase import create_client, Client


# Initialize Supabase client
SUPABASE_URL = "https://adqhjaqlidqbiqltwhpk.supabase.co"  # Replace with your Supabase project URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFkcWhqYXFsaWRxYmlxbHR3aHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjkzMjc3MDgsImV4cCI6MjA0NDkwMzcwOH0.O3MVZ-FTnR43E6GYgguGn_hl3uWrv6bu3pYkVLIrNkI"  # Replace with your Supabase project API key
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

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
        st.switch_page("Login.py")
    except Exception as e:
        st.error(f"Sign-up failed: {e}")

