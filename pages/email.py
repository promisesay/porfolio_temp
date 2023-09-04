from send_email import *
import streamlit as st


st.header('contact us')
with st.form('userData'):
    user_email = st.text_input('write an email')
    selectBox = st.selectbox("what is the topic?", ["designing", "photography", "mdf job stiller"])
    if selectBox == "mdf job stiller":
        selectBox = st.text_input("who?!!")
    raw_message = st.text_area('massage')
    submit = st.form_submit_button("submit")
    message = f"""\
Subject: a new message from {user_email}
    
From: {user_email}
{raw_message}
"""
    if submit:
        print('ok')
        send_email(message)
        st.info("email send successfully")

