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
 
st.markdown('---')   

# Checkbox widget
st.subheader('st.checkbox')
is_agreed = st.checkbox('I agree to terms and conditions')  # returns bool
st.write('checkbox status: {}'.format(is_agreed))

# Multiple checkboxes
with st.container():
    st.info('What technologies do you use?')
    
    python = st.checkbox('Python')
    datascience = st.checkbox('Data Science')
    ai_ml = st.checkbox('AI/ML')
    andorid = st.checkbox('Andorid')
    react = st.checkbox('React JS')
    java = st.checkbox('Core Java')
    javascript = st.checkbox('Javascript')
    
    tech_button = st.button('Submit')
    
    if tech_button:
        tech_dict = {
            'Python': python,
            'Data Science': datascience,
            'AI/ML': ai_ml,
            'Android': andorid,
            'React JS': react,
            'Core Java': java,
            'Javasript': javascript,
        }
        st.json(tech_dict)