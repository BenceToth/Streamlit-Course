import streamlit as st
from datetime import datetime

with st.form('myform'):
    st.subheader('Registration Form')

    # Name
    name_col1, name_col2, name_col3 = st.columns(3)

    title = name_col1.selectbox(label='', options=('Mr', 'Mrs', 'Miss'))
    first_nm = name_col2.text_input('First Name')
    last_nm = name_col3.text_input('Last Name')

    # Role
    role = st.selectbox('Role', ('Software', 'Sr. Software', 'Technical Lead',
                                'Manager', 'Sr. Manager', 'Project Manager'))

    # Date of Birth
    dob = st.date_input('Date of Birth', 
                        min_value=datetime(year=1900,month=1,day=1))

    # Gender
    gender = st.radio('Select Gender',
                      ('Male', 'Female', 'Prefer not to say'))

    # Age
    age = st.slider('Age', min_value=1, max_value=100, value=30, step=1)

    has_submitted = st.form_submit_button('Submit')

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