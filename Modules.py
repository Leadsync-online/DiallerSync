import streamlit as st
from supabase import create_client, Client
import pandas as pd
import csv
import os

# Initialize Supabase client
SUPABASE_URL = "https://adqhjaqlidqbiqltwhpk.supabase.co" # Replace with your Supabase project URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFkcWhqYXFsaWRxYmlxbHR3aHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjkzMjc3MDgsImV4cCI6MjA0NDkwMzcwOH0.O3MVZ-FTnR43E6GYgguGn_hl3uWrv6bu3pYkVLIrNkI" # Replace with your Supabase project API key
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
def detect_delimiter(file):
    """Detects the delimiter of a CSV/TXT file."""
    sample = file.read(1024).decode('utf-8')
    file.seek(0)
    sniffer = csv.Sniffer()
    delimiter = sniffer.sniff(sample).delimiter
    return delimiter

def read_file(uploaded_file):
    """Reads an uploaded file (CSV, TXT, Excel) while auto-detecting its type and delimiter."""
    ext = uploaded_file.name.split('.')[-1].lower()
    
    if ext in ['xls', 'xlsx']:
        df = pd.read_excel(uploaded_file)
    elif ext in ['csv', 'txt']:
        delimiter = detect_delimiter(uploaded_file)
        df = pd.read_csv(uploaded_file, delimiter=delimiter)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV, TXT, or Excel file.")
    
    return df

def get_table_columns(table_name):
    """Fetches the table columns from Supabase and returns a DataFrame."""
    response = supabase.table(table_name).select("idnumber,agent_id,call_start,call_end,duration,disposition,disposition_discription,phone_number").limit(1).execute()    
    if hasattr(response, "error") and response.error:
        st.error(f"Error fetching columns: {response.error}")
        return pd.DataFrame()    
    if response.data:
        columns = response.data[0].keys()
    else:
        columns = []
    return pd.DataFrame(columns=columns)


# def map_fields_to_supabase(df, table_name):
#     """Allows users to map fields from the uploaded file to Supabase table columns within a form."""
#     df_columns = df.columns.tolist()
#     st.dataframe(df_columns.head(3))
#     supabase_table = get_table_columns(table_name)
    
    # if supabase_table.empty:
    #     st.error("Failed to fetch Supabase table columns. Please check your connection or table name.")
    #     return

    # supabase_columns = supabase_table.columns.tolist()
    # field_mapping = {}

    # with st.form(key="mapping_form"):
    #     st.write("### Map Fields to Supabase Table")
    #     for col in supabase_columns:
    #         field_mapping[col] = st.selectbox(f"Select mapping for {col}", ["Ignore"] + df_columns, index=0)
    #     submit_button = st.form_submit_button(label="Upload to Supabase")

    # if submit_button:
    #     mapped_data = df.rename(columns={v: k for k, v in field_mapping.items() if v != "Ignore"})
    #     data = mapped_data.to_dict(orient='records')
    #     response = supabase.table(table_name).insert(data).execute()
        
    #     if isinstance(response, dict) and "error" in response:
    #         st.error(f"Error inserting data: {response['error']}")
    #     else:
    #         st.success("Data successfully uploaded to Supabase!")
