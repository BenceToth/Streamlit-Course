import streamlit as st 
import pandas as pd 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os

# Sidebar
with st.sidebar:
    uploaded_file = st.file_uploader('Upload a .csv or .xlsx file (not exceeding 10 MB)')
    
if uploaded_file is not None:
    # Load .csv file
    df = pd.read_csv(uploaded_file)
    
    st.dataframe(df.head())