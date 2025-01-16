import streamlit as st
import pandas as pd
import time

# Sidebar object
side_bar = st.sidebar

# Passing elements to sidebar
side_bar.header('st.sidebar')
side_bar.caption('Elements that are added to the sidebar are pinned to the left')

# Load tips.csv
df = pd.read_csv('tips.csv')

df_columns = tuple(df.columns)
st.write(df_columns)

# Create a Selectbox widget
selected_column = side_bar.selectbox(
    "Select the column you want to display",
    df_columns
)

side_bar.write('Your selected column is: {}'.format(selected_column))

# Display df
st.dataframe(df[[selected_column]])