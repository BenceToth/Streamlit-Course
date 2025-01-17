import streamlit as st
import pandas as pd
import numpy as np
# static
import matplotlib.pyplot as plt
import seaborn as sns

import os

st.title('Matplotlib and Seaborn Visualizations in Streamlit')

# data load
df = pd.read_csv('./tips.csv')

st.dataframe(df.head())

## Questions
st.markdown('---')

with st.container():
    st.header('1. Find the distribution of males and females (pie and bar charts)')
    value_counts = df['sex'].value_counts()
    
    col1, col2 = st.columns(2)
    # Pie Chart
    with col1:
        st.subheader('Pie Chart')
        fig, ax = plt.subplots()
        ax.pie(value_counts, labels=value_counts.index, autopct='%0.2f%%')
        st.pyplot(fig)
    # Bar Chart
    with col2:
        st.subheader('Bar Chart')
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)
        
    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)

## 2. Find the distribution of spending by males and females (boxplot or kdeplot)
## 3. Find the distribution of average total_bill across each day by males and females
## 4. Find the relationship between total_bill and tip over time (scatter plot)
