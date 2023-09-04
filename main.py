import streamlit as st
import pandas as pa
st.set_page_config(layout='wide')
context = '''
here are some amigoes hanging around in the universe without any responsibility but good pictures duo..?!
'''
st.header("welcome to nothing")
st.info(context)
col1, empty_col, col2, empty_coil, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pa.read_csv("data.csv")
print(df)
with col1:
    for index, i in df[:4].iterrows():
        st.subheader(i['role'])
        st.image('images/'+i['image'])
        st.info(i['first name']+' '+i['last name'])

with col2:
    for index, i in df[4:8].iterrows():
        st.subheader(i['role'])
        st.image('images/'+i['image'])
        st.info(i['first name']+' '+i['last name'])

with col3:
    for index, i in df[8:].iterrows():
        st.subheader(i['role'])
        st.image('images/'+i['image'])
        st.info(i['first name']+' '+i['last name'])

