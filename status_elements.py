import streamlit as st
import time

# Progress Bar
st.header('st.progress')
st.caption('Display a progress bar')

def show_progbar():
    # update value in loop
    for pct_complete in range(1, 121, 20):
        time.sleep(0.5)
        pct_complete = min(pct_complete, 100)
        my_bar.progress(pct_complete)
    
# Spinner
with st.spinner("Something is processing"):
    my_bar = st.progress(0)
    show_progbar()