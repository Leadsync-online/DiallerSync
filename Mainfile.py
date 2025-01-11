import streamlit as st
from supabase import create_client, Client
import streamlit_authenticator as stauth
import json

# Initialize Supabase
SUPABASE_URL = "https://your-supabase-url.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def login_screen():
    st.title("Login")
    
    # Google Login
    google_button = oauth.google_button("Log in with Google")
    if google_button:
        user_info = oauth.get_user_info()
        st.success(f"Welcome {user_info['email']}!")

    st.write("---")
    
    # Username/Password Login
    st.subheader("Login with Username and Password")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        auth_response = supabase.auth.sign_in_with_password(
            email=username, password=password
        )
        if auth_response:
            st.success(f"Welcome back, {username}!")
        else:
            st.error("Invalid credentials. Please try again.")

    st.write("---")
    
    if st.button("Sign Up"):
        st.session_state["screen"] = "signup"

def signup_screen():
    st.title("Sign Up")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if password != confirm_password:
            st.error("Passwords do not match.")
        else:
            response = supabase.auth.sign_up(email=email, password=password)
            if response:
                st.success("Account created successfully! You can now log in.")
                st.session_state["screen"] = "login"
            else:
                st.error("Error signing up. Please try again.")

    if st.button("Back to Login"):
        st.session_state["screen"] = "login"

# Main Streamlit App
if "screen" not in st.session_state:
    st.session_state["screen"] = "login"

if st.session_state["screen"] == "login":
    login_screen()
elif st.session_state["screen"] == "signup":
    signup_screen()

