import streamlit as st
from supabase import create_client, Client

# Initialize Supabase client
SUPABASE_URL = "https://adqhjaqlidqbiqltwhpk.supabase.co"  # Replace with your Supabase project URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFkcWhqYXFsaWRxYmlxbHR3aHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjkzMjc3MDgsImV4cCI6MjA0NDkwMzcwOH0.O3MVZ-FTnR43E6GYgguGn_hl3uWrv6bu3pYkVLIrNkI"  # Replace with your Supabase project API key
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Hide Streamlit sidebar and other UI elements
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
    }
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Define login and signup functions
def login(username, password):
    try:
        user = supabase.auth.sign_in_with_password({"email": username, "password": password})
        return user
    except Exception:
        st.error("Login failed. Check your username and password.")
        return None

def signup(username, password):
    try:
        user = supabase.auth.sign_up({"email": username, "password": password})
        st.success("Sign-up successful! You can now log in.")
        st.switch_page("Login")
    except Exception as e:
        st.error(f"Sign-up failed: {e}")

# Main app layout
def main():
    st.title("Welcome to My App")
    st.write("Log in or sign up to continue.")

    # Login form
    st.subheader("Login")
    username = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        user = login(username, password)
        if user:
            st.session_state["user"] = user
            st.success("Logged in successfully!")
            st.switch_page("Mainfile")

    # Sign-up button
    if st.button("Sign Up"):
        st.switch_page("Sign Up")

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

# Handle page routing
if "page" not in st.session_state:
    st.session_state["page"] = "Login"

if st.session_state["page"] == "Login":
    main()
elif st.session_state["page"] == "Sign Up":
    signup_page()
