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
    [data-testid="stSidebarCollapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    st.header("Dashboard")

with col4:
    st.text("")
    if st.button("Settings", use_container_width=True):
        st.switch_page("pages/Settings.py")

with st.container(border=True):
    col5, col6, col7 = st.columns(3)
    
    with col5:
        st.selectbox(
        "Please select campaign?",
        ("Onair", "MTN", "Mobile phone"))
    
    with col6:
        st.date_input("Please select date?", today)
    
    with col7:
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

st.subheader("Agent Statistics", divider=False)

p,q,r,s  = st.columns(4)

p.metric("Average Agents", "5", "5", border=True)
q.metric("New Agents", "1", "1", border=True)
r.metric("Old Agents", "4", "5", border=True)
s.metric("Average Agent Tenure", "100", "10", border=True)

with st.container(border=True):
    st.write("Agents per hour")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)

st.subheader("Disposition Statistics", divider=False)

t,u,v,w  = st.columns(4)

t.metric("Contact", "2000", "2000", border=True)
u.metric("Non Contact", "3000", "3000", border=True)
v.metric("Voice mails", "1000", "1000", border=True)
w.metric("Average sec voice mail", "5", "4", border=True)

with st.container(border=True):
    st.write("Voice mails per hour")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)
    
with st.container(border=True):
    st.write("Dispositions")
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df) 
