import streamlit as st
from supabase import create_client, Client
import Modules as md
from datetime import date, timedelta
import pandas as pd
import numpy as np

today = date.today()

st.set_page_config(initial_sidebar_state="collapsed",layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"]{
        visibility: hidden;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

st.header("Dashboard")

with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.selectbox(
        "Please select campaign?",
        ("Onair", "MTN", "Mobile phone"))
    
    with col2:
        st.date_input("Please select date?", today)
    
    with col3:
        st.text("")
        if st.button("Import file", use_container_width=True):
            st.switch_page("pages/Import.py")

st.subheader("Dialler Statistics", divider=False)

a,b,c,d  = st.columns(4)

a.metric("Total dials", "10000", "9000", border=True)
b.metric("Distinct dials", "5000", "4000", border=True)
c.metric("Average contact per Agent", "100", "100", border=True)
d.metric("Average wait time", "15", "16", border=True)

e,f,g,k  = st.columns(4)

e.metric("Average Talk Time", "40", "30", border=True)
f.metric("Average Ring time", "20", "25", border=True)
g.metric("Contact Rate", "15", "20", border=True)
k.metric("Distinct Contact Rate", "20", "30", border=True)

with st.container(border=True):
    st.write("Average talk time")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)

with st.container(border=True):
    st.write("Average Contact Rate")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)

st.subheader("CLI Statistics", divider=False)

l,m,n,o  = st.columns(4)

l.metric("Number of CLI's", "5", "5", border=True)
m.metric("Average CLI Usage", "5000", "4000", border=True)
n.metric("Newest CLI", "10", "1", border=True)
o.metric("Oldest CLI", "100", "10", border=True)

with st.container(border=True):
    st.write("CLI Utilization")
    chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )
    
    st.line_chart(chart_data, x="col1", y="col2", color="col3")
