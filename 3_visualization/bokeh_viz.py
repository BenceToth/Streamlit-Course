import streamlit as st
import pandas as pd
# Bokeh
from bokeh.plotting import figure

x = [1,2,3,4,5]
y = [6,7,2,4,5]

p = figure(title='Simple Line Chart',
           x_axis_label='x',
           y_axis_label='y')

p.line(x, y, line_width=2)
p.circle(x, y, fill_color='white', size=10)

st.bokeh_chart(p)