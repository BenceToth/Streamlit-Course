import streamlit as st
import time
import numpy as np

st.write("streamlit version = {}".format(st.__version__))

# Init Progress Bar
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Init Chart
last_rows = np.random.randn(1,1)
chart = st.line_chart(last_rows)

# Generate synthetic data
for i in range(1, 101):
    new_rows = last_rows[-1,:] + np.random.randn(5,1)
    status_text.text("%i%% Complete"%i)
    progress_bar.progress(i)
    
    time.sleep(0.1)
    
progress_bar.empty()