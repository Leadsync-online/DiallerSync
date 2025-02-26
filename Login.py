import streamlit as st
from supabase import create_client, Client
import Modules as md

# Hide Streamlit sidebar and other UI elements
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
    st.write("Log in or sign up to continue.")
    
# Main app layout
def main():

    col1, col2, col3 = st.columns([1,7,1])  # Adjust column ratios as needed
    with col2:
    # Login form
        username = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login ", use_container_width=True):
            user = md.login(username, password)
            if user:
                st.session_state["user"] = user
                st.success("Logged in successfully!")
                st.switch_page("pages/Home.py")
    # Sign-up button
        if st.button("Signup", use_container_width=True):
            st.switch_page("pages/Signup.py")

# Handle page routing
main()
