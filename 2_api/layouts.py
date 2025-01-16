import streamlit as st
import pandas as pd
import time

# Sidebar object
side_bar = st.sidebar

# Passing elements to sidebar
side_bar.header('st.sidebar')
side_bar.caption('Elements that are added to the sidebar are pinned to the left')
side_bar.write('This is a sidebar')

# Passing elements to the main page
st.write('This is the main page')