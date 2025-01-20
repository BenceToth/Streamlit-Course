import streamlit as st 
import pandas as pd 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os

st.set_page_config(page_title='Data Profiler', page_icon=':bar_chart:', layout='wide', initial_sidebar_state='expanded')

# Sidebar
with st.sidebar:
    uploaded_file = st.file_uploader('Upload a .csv or .xlsx file (not exceeding 10 MB)')
    
if uploaded_file is not None:
    # Load .csv file
    df = pd.read_csv(uploaded_file)
    
    # Generate report
    with st.spinner('Generating Report...'):
        pr = ProfileReport(df)
        
    st_profile_report(pr)