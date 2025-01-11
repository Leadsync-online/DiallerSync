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
            st.switch_page("pages/Home.py")

    # Sign-up button
    if st.button("Signup"):
        st.switch_page("pages/Signup.py")

# Handle page routing
if "page" not in st.session_state:
    st.session_state["page"] = "Login"

if st.session_state["page"] == "Login":
    main()
elif st.session_state["page"] == "Signup":
    signup_page()
