import streamlit as st
import os
import tabula
import pandas
import subprocess
import webbrowser
import matplotlib.pyplot as plt
from individualPage import individualAnalysis
from combinedPage import combinedAnalysis
from fileUpload import uploadFile
from dataCleaning import cleaning

st.image('Somaiya Header.png',width=500)
st.title('Result analysis')
st.subheader('K. J. Somaiya Institute Of Engineering And Information Technology')
st.sidebar.title('Welcome to the Result Evaluation & Analyser Streamlit App')
st.sidebar.markdown('<html><body style="background-color:yellow;"> You can Do <b>Visual</b> or <b>Database</b> analysis as you wish after filling the parameters select as required </body></html>',unsafe_allow_html=True)
# Analyse_type=st.sidebar.radio('Analyser',('Visual','Database Analyser','Repo

filename = uploadFile()
st.write(filename)
pd_df = cleaning(filename)
Analyse_type=st.sidebar.radio('Analyser',('Combined Result','Individual Analysis'))
if Analyse_type=='Combined Result':
    combinedAnalysis(pd_df)
if Analyse_type=='Individual Analysis':
    if filename==None:
        print("No file selected")
    else:
        individualAnalysis(pd_df,filename)