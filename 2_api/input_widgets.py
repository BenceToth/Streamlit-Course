import streamlit as st
import pandas as pd
import numpy as np
import os

# load data
tips_df = pd.read_csv('tips.csv')

def display_random_sample(df):
    sample_data = df.sample(5)
    return sample_data


# Button widget
st.subheader('Display 5 random rows from tips.csv')
st.caption('Click on the button below to display the rows randomly')
button = st.button('Display random 5 rows')

if button:
    sample_tips = display_random_sample(tips_df)
    st.dataframe(sample_tips)