import streamlit as st
import pandas as pd
import numpy as np
np.bool = np.bool_
# Bokeh
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

x = [1,2,3,4,5]
y = [6,7,2,4,5]

p = figure(title='Simple Line Chart',
           x_axis_label='x',
           y_axis_label='y')

p.line(x, y, line_width=2)
p.circle(x, y, fill_color='white', size=10)

st.bokeh_chart(p)

st.markdown('---')
# 1. Draw a scatter plot between total bill and tip
df = pd.read_csv('tips.csv')

st.subheader('1. Draw a scatter plot between total bill and tip')
p = figure(title='Scatter plot between total bill vs tips')
p.circle(x='total_bill', y='tip', source=df, size=12)
st.bokeh_chart(p)


st.markdown('---')
# 2. Draw a scatter plot between total bill and tip, and color by options
st.subheader('2. Draw a scatter plot between total bill and tip, and color by options')

p = figure(title='Scatter plot, colored by categories')
select = st.selectbox('Select the categories', ('sex', 'day', 'smoker', 'time'))

color_palette = ['blue', 'red', 'green', '#D35400', 'black']
unique_cats = df[select].unique()
index_cmap = factor_cmap(select, 
                         palette=color_palette[:len(unique_cats)], 
                         factors=sorted(unique_cats))

p.circle(x='total_bill', y='tip', source=df, fill_color=index_cmap, size=12, legend=select)
st.bokeh_chart(p)