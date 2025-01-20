import streamlit as st 
import pandas as pd 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os

st.set_page_config(page_title='Data Profiler', page_icon=':bar_chart:', layout='wide', initial_sidebar_state='expanded')

# Sidebar
with st.sidebar:
    uploaded_file = st.file_uploader('Upload a .csv or .xlsx file (not exceeding 10 MB)', type=['csv', 'xlsx'], accept_multiple_files=False)
    if uploaded_file is not None:
        st.write('Modes of Operation')
        minimal = st.checkbox('Do you want to display a minimal report?')
        display_mode = st.radio('Select Display Mode', 
                                options=('Primary', 'Dark', 'Orange'))
        
        if display_mode == 'Dark':
            theme = 'flatly'
            primary_colors = ['black']
        elif display_mode == 'Orange':
            theme = 'united'
            primary_colors = ['orange']
        else:
            theme = None
            primary_colors = ['blue']
    
if uploaded_file is not None:
    # Load .csv file
    df = pd.read_csv(uploaded_file)
    
    # Generate report
    with st.spinner('Generating Report...'):
        pr = ProfileReport(df, minimal=minimal,
                           html={'style': {'theme': theme,
                                           'primary_colors': primary_colors}})
        
    st_profile_report(pr)