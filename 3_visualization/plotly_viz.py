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
st.plotly_chart(fig, key='chart1')

st.markdown('---')
# 3. Draw a histogram of the total bill, and color by (sex, smoker, day, time)
st.subheader('3. Draw a a scatterplot between total bill and tips, and color by categorical features')

selector = st.selectbox('Select a feature to color by', 
                        ('sex', 'smoker', 'day', 'time'))

fig = px.histogram(data_frame=df, x='total_bill', color=selector)
st.plotly_chart(fig, key='chart2')

st.markdown('---')
# 4. Draw a a scatterplot between total bill and tips, and color by ('sex', 'smoker', 'day', 'time')
st.subheader('4. Draw a a scatterplot between total bill and tips, and color by (sex, smoker, day, time)')

color_option = st.selectbox('Select a column to color by', 
                           ('sex', 'smoker', 'day', 'time'))

fig = px.scatter(data_frame=df, x='total_bill', y='tip', color=color_option)
st.plotly_chart(fig, key='chart3')

# 5. Draw a Sunburst Chart on features ('sex', 'smoker', 'day', 'time')
st.markdown('---')
st.subheader('5. Draw a Sunburts Chart on features (sex, smoker, day, time)')

path = st.multiselect('Select the categorical feature path',
                     ('sex', 'smoker', 'day', 'time'))

fig = px.sunburst(data_frame=df, path=path)
st.plotly_chart(fig, key='chart4')