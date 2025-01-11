import streamlit as st
from supabase import create_client, Client
import Modules as md

# Hide Streamlit sidebar and other UI elements
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# Main app layout
def main():
    st.title("Dialler Sync")
    st.write("Log in or sign up to continue.")

    # Login form
    st.subheader("Login")
    username = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        user = md.login(username, password)
        if user:
            st.session_state["user"] = user
            st.success("Logged in successfully!")
            st.switch_page("pages/Home.py")

    # Sign-up button
    if st.button("Signup"):
        st.switch_page("pages/Signup.py")

# Handle page routing
main()
