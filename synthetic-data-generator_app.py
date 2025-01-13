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