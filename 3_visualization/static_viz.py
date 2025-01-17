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

st.markdown('---')
## 3. Find the distribution of average total_bill across categorical features
with st.container():
    st.header('3. Find the distribution of average total_bill across categorical features')
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        group_cols = st.multiselect(label='Select features', options=cat_cols, default=cat_cols[0])
        n_features = len(group_cols)
    with c2:
        chart_type = st.selectbox('Select a chart type', ['bar', 'area', 'line'])
    with c3:
        stack_option = st.radio('Stack?', ('Yes', 'No'))
        if stack_option == 'Yes':
            is_stacked = True
        else:
            is_stacked = False
        
    feature_to_avg = ['total_bill']
    avg_total_bill = df.groupby(group_cols)[feature_to_avg].mean()
    
    if n_features > 1:
        for i in range(n_features-1):
            avg_total_bill = avg_total_bill.unstack(fill_value=0)
    
    # Visualize
    fig, ax = plt.subplots()
    avg_total_bill.plot(kind=chart_type, ax=ax, stacked=is_stacked)
    ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax.set_ylabel('Avg Total Bill')
    st.pyplot(fig)

    with st.expander('Click here to display values'):
        st.dataframe(avg_total_bill)

st.markdown('---')
## 4. Find the relationship between total_bill and tip over time (scatter plot)
with st.container():
    st.header('4. Find the relationship between total_bill and tip over time (scatter plot)')
    fig, ax = plt.subplots()
    hue_type = st.selectbox('Select the feature to hue', cat_cols)
    sns.scatterplot(x='total_bill', y='tip', hue=hue_type, ax=ax, data=df)
    st.pyplot(fig)