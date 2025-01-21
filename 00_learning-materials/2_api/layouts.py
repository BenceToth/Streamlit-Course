import streamlit as st
import pandas as pd
import time

# Layout: Sidebar

## Sidebar object
side_bar = st.sidebar

## Passing elements to sidebar
side_bar.header('st.sidebar')
side_bar.caption('Elements that are added to the sidebar are pinned to the left')

## Load tips.csv
df = pd.read_csv('tips.csv')

df_columns = tuple(df.columns)
st.write(df_columns)

## Create a Selectbox widget
selected_column = side_bar.selectbox(
    "Select the column you want to display",
    df_columns
)

side_bar.write('Your selected column is: {}'.format(selected_column))

## Display df
st.dataframe(df[[selected_column]])


# Layout: Columns
st.header('st.columns')
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('This is my first column')
    st.image('./media/image.jpg')
    
with col2:
    st.subheader('This is my second column')
    st.dataframe(df)
    
with col3:
    st.subheader('This is my third column')
    st.dataframe(df[[selected_column]])
    
# Layout: Expander
st.header('st.expander')

with st.expander('This is my Expander'):
    st.write("""
        Insert a multi-element container that can be expanded/collapsed.
        
        Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed by the user.
        When collapsed, all that is visible is the provided label.
    """)
    
    st.code("""
        # you can create an expander with st.expander
        import streamlit as st
        st.expander('some message')
    """, language='python')
    
# Layout: Container
st.header('st.container')

with st.container():
    st.write('This text is inside a container')

# Layout: Empty
st.header('st.empty')

placeholder = st.empty()

for i in range(10, 0, -1):
    placeholder.write('This message will disappear in {} seconds'.format(i))
    time.sleep(1)

placeholder.empty()

