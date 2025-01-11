import streamlit as st
from supabase import create_client, Client

# Initialize Supabase client
SUPABASE_URL = "https://adqhjaqlidqbiqltwhpk.supabase.co"  # Replace with your Supabase project URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFkcWhqYXFsaWRxYmlxbHR3aHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjkzMjc3MDgsImV4cCI6MjA0NDkwMzcwOH0.O3MVZ-FTnR43E6GYgguGn_hl3uWrv6bu3pYkVLIrNkI"  # Replace with your Supabase project API key
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Hide Streamlit sidebar
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Define login and signup functions
def login(username, password):
    try:
        user = supabase.auth.sign_in_with_password({"email": username, "password": password})
        return user
    except Exception as e:
        st.error("Login failed. Check your username and password.")
        return None

def signup(username, password):
    try:
        user = supabase.auth.sign_up({"email": username, "password": password})
        st.success("Sign-up successful! Please log in.")
        return user
    except Exception as e:
        st.error(f"Sign-up failed: {e}")
        return None

# Define main app layout
def main():
    st.title("Streamlit Supabase Authentication")

    # Login and Signup form selector
    auth_action = st.sidebar.radio("Select Action", ("Login", "Sign Up"))

    if auth_action == "Login":
        st.header("Login")
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = login(username, password)
            if user:
                st.session_state["user"] = user
                st.success("Logged in successfully!")
                st.experimental_set_query_params(page="Home")
                st.experimental_rerun()

    elif auth_action == "Sign Up":
        st.header("Sign Up")
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Sign Up"):
            signup(username, password)

# Handle page navigation
def navigate_to_home():
    st.experimental_set_query_params(page="Home")
    st.experimental_rerun()

if "user" not in st.session_state:
    main()
else:
    navigate_to_home()
