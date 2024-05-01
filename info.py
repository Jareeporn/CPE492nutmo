import streamlit as st


st.title('Information about Orchids')

# ข้อมูลที่จะแสดงใน selectbox
options = ['Option 1', 'Option 2', 'Option 3']

# เลือกข้อมูลจาก selectbox
selected_option = st.selectbox('เลือกข้อมูล', options)

# แสดงข้อมูลที่ถูกเลือก
st.write('คุณเลือก:', selected_option)
