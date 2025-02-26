import streamlit as st
from supabase import create_client, Client
import pandas as pd
import csv
import os

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
        st.success("Please verify your email before logging in.")
        st.switch_page("Login.py")
    except Exception as e:
        st.error(f"Sign-up failed: {e}")

# File checker
def detect_delimiter(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        sample = file.read(1024)
        sniffer = csv.Sniffer()
        delimiter = sniffer.sniff(sample).delimiter
        return delimiter

def read_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    
    if ext in ['.xls', '.xlsx']:
        df = pd.read_excel(file_path)
    elif ext in ['.csv', '.txt']:
        delimiter = detect_delimiter(file_path)
        df = pd.read_csv(file_path, delimiter=delimiter)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV, TXT, or Excel file.")
    
    return df
