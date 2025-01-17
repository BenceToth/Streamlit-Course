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