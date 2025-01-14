import streamlit as st

# Title
st.title('This is a Title')
st.caption('Using st.title() you can display a text in title format')

# Header
st.header('This is a Header')
st.caption('The text inside st.header() is in header format')

# Subheader
st.subheader('This is a Subheader')
st.caption('The text inside st.subheader() is in subheader formatting')


# Display code on page
st.markdown('---')
st.subheader('Generate random numbers')
body = """
import numpy as np

def generate_random(size):
    rand = np.random.random(size=size)
    return rand
    
number = generate_random(10)
"""
st.code(body, language='python')

# Latex
st.markdown('---')
st.subheader('Latex')

formula = """
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} a r^k
"""
st.latex(formula)