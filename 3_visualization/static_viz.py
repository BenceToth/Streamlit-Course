import streamlit as st
import pandas as pd
import numpy as np
# static
import matplotlib.pyplot as plt
import seaborn as sns

st.header('Matplotlib and Seaborn Visualizations in Streamlit')

# data load
df = pd.read_csv('./tips.csv')

st.dataframe(df.head())

st.markdown('---')

# Questions
## 1. Show the distribution of a categorical feature (pie and bar charts)

# Categorical columns in df
data_types = df.dtypes
cat_cols = data_types[data_types == 'object'].index

with st.container():
    st.header('1. Show the distribution of a categorical feature (pie and bar charts)')
    
    # Select feature
    feature = st.selectbox('Select a feature you want to display on the charts', cat_cols)
    value_counts = df[feature].value_counts()
    
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
        
    # Display value counts
    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)
        
        
st.markdown('---')
## 2. Find the distribution of spending by males and females (boxplot or kdeplot)
with st.container():
    st.header('2. Find the distribution of spending by males and females (various plots)')
    
    # Select chart
    chart = ('box', 'violin', 'kdeplot', 'histogram')
    chart_selection = st.selectbox('Select a chart type', chart)
    
    fig, ax = plt.subplots()
    if chart_selection == 'box':
        sns.boxplot(x='sex', y='total_bill', data=df, ax=ax)
    elif chart_selection == 'violin':
        sns.violinplot(x='sex', y='total_bill', data=df, ax=ax)
    elif chart_selection == 'kdeplot':
        sns.kdeplot(x='total_bill', hue='sex', data=df, shade=True, ax=ax)
    elif chart_selection == 'histogram':
        sns.histplot(x='total_bill', hue='sex', data=df, ax=ax)

    st.pyplot(fig)

## 3. Find the distribution of average total_bill across each day by males and females
## 4. Find the relationship between total_bill and tip over time (scatter plot)