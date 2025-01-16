import streamlit as st
import time

# Progress Bar
st.header('st.progress')
st.caption('Display a progress bar')

my_bar = st.progress(0)

# update value in loop
for pct_complete in range(1, 101):
    time.sleep(0.5)
    my_bar.progress(pct_complete)