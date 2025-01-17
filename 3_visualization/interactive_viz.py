import streamlit as st
import pandas as pd
import numpy as np

sample_df = pd.DataFrame(np.random.randint(low=10, high=20, size=(5,3)),
                         columns=['A', 'B', 'C'])

# Bar Plot
st.bar_chart(sample_df)

# Area Plot
st.area_chart(sample_df)

# Line Plot
st.line_chart(sample_df)