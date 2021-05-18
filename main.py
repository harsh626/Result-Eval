import streamlit as st
import os
import tabula
import pandas as pd
import subprocess
import webbrowser
import matplotlib.pyplot as plt
from pages import cleaning, uploadFile, combinedAnalysis, individualAnalysis, passfail

st.image('Somaiya Header.png',width=500)
st.title('Result analysis')
st.subheader('K. J. Somaiya Institute Of Engineering And Information Technology')
st.sidebar.title('Welcome to the Result Evaluation Web app')

filename = uploadFile()
st.write(filename)

pd_df = cleaning(filename)
pa_df = passfail(filename)

Analyse_type=st.sidebar.radio('Analyser',('Combined Result','Individual Analysis'))

if Analyse_type=='Combined Result':
    combinedAnalysis(pd_df,pa_df)

if Analyse_type=='Individual Analysis':
    if filename==None:
        print("No file selected")
    else:
        individualAnalysis(pd_df,filename)