import streamlit as st

def uploadFile():
    filename = None
    filename = st.text_input('Enter a file path:','Cleaned Marksheet.xlsx')
    return filename