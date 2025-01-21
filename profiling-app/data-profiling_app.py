import streamlit as st 
import pandas as pd 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os

st.set_page_config(page_title='Data Profiler', page_icon=':bar_chart:', layout='wide', initial_sidebar_state='expanded')

def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext in ('.csv', '.xlsx'):
        return ext
    else:
        False

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
    # validate extension
    ext = validate_file(uploaded_file)
    
    # Load .csv file
    if ext:
        if ext == '.csv':
            df = pd.read_csv(uploaded_file)
        else:
            xl_file = pd.ExcelFile(uploaded_file)
            sheet_tuple = tuple(xl_file.sheet_names)
            sheet_name = st.sidebar.selectbox('Select the sheet', sheet_tuple)
            df = xl_file.parse(sheet_name)
    
        # Generate report
        with st.spinner('Generating Report...'):
            pr = ProfileReport(df, minimal=minimal,
                            html={'style': {'theme': theme,
                                            'primary_colors': primary_colors}})
            
        st_profile_report(pr)
    else:
        st.error('Please only upload an .csv or .xlsx file!')