import streamlit as st
from supabase import create_client, Client
#import Modules as md

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
