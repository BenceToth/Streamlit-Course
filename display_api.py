import streamlit as st
import pandas as pd
import numpy as np

# display text
st.write("Hello World")

st.write("Welcome to Streamlit APIs")

# display integers
st.write(1234)

# display pandas DF
df = pd.DataFrame({
    'first_column': [1,2,3,4],
    'second_column': [10,20,30,40]
})

st.write(df)

# display numpy array
st.write(np.array([1,2,3,4]))