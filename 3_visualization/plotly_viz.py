import streamlit as st
import pandas as pd
import numpy as np
# Plotly
import plotly.express as px


df = pd.read_csv('tips.csv')

# Reference URL: https://plotly.com/python/plotly-express/
# 1. Draw a histogram of the total bill
st.subheader('1. Draw a histogram of the total bill')
fig = px.histogram(data_frame=df, x='total_bill')
st.plotly_chart(fig)

st.markdown('---')
# 2. Draw a histogram of the total bill, and color by sex
st.subheader('2. Draw a histogram of the total bill, and color by sex')
fig = px.histogram(data_frame=df, x='total_bill', color='sex')
st.plotly_chart(fig)
# 3. Draw a a scatterplot between total bill and tips, and color by ('sex', 'smoker', 'day', 'time')
# 4. Draw a Sunburts Chart on features ('sex', 'smoker', 'day', 'time')