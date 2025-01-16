import streamlit as st

st.header('Registration Form')

name_container = st.container()
with name_container:
    
    name_col1, name_col2, name_col3 = st.columns(3)
    
    with name_col1:
        title = st.selectbox(label='', options=('Mr', 'Mrs', 'Miss'))
        
    with name_col2:
        first_nm = st.text_input('First Name')
        
    with name_col3:
        last_nm = st.text_input('Last Name')
        

role = st.selectbox('Role', ('Software', 'Sr. Software', 'Technical Lead',
                             'Manager', 'Sr. Manager', 'Project Manager'))

dob = st.date_input('Date of Birth', value='1990-01-01')

gender = st.radio('Select Gender', ('Male', 'Female', 'Prefer not to say'))

age = st.slider('Age', min_value=1, max_value=100, value=30, step=1)

has_submitted = st.button('Submit')

if has_submitted:
    st.success('Form submitted successfully')
    info = {
        'Name': ' '.join([title, first_nm, last_nm]),
        'Age': age,
        'Gender': gender,
        'Date of Birth': dob,
        'Role': role 
    }
    st.json(info)
    
    
