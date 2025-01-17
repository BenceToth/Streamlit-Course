import streamlit as st
import pandas as pd
import numpy as np
# static
import matplotlib.pyplot as plt
import seaborn as sns

import os

st.header('Matplotlib and Seaborn Visualizations in Streamlit')

# data load
df = pd.read_csv('./tips.csv')

st.dataframe(df.head())

## Questions
## 1. Find the distribution of males and females (pie and bar charts)
## 2. Find the distribution of spending by males and females (boxplot or kdeplot)
## 3. Find the distribution of average total_bill across each day by males and females
## 4. Find the relationship between total_bill and tip over time (scatter plot)
