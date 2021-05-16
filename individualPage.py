import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


from data import create_database,fire_query
def individualAnalysis(pd_df,filename):
    st.title("Individual Analysis")
    st.write("adfbvu")
    query = st.text_input('Enter a sql query:','select * from `Cleaned Marksheet`')
    # query = "select * from `Cleaned Marksheet` where Names='AAYUSHI VAIBHAV MEHTA'"
    create_database(filename,pd_df)
    individual_df = fire_query(query,filename)
  
    st.write(individual_df.T)
    # theory_df = individual_df.values[0][1:7]
    # term_work_df = individual_df.values[0][8:]
    #pd_df.loc[sr_no].to_frame().T


    #radar graph
    if len(individual_df)==1:
        theory_df = pd.DataFrame(dict(
            marks=individual_df.values[0][1:7],
            Subjects=individual_df.columns[1:7]))
        term_work_df = pd.DataFrame(dict(
            marks=individual_df.values[0][8:],
            Subjects=individual_df.columns[8:]))
        theory_fig = px.line_polar(theory_df, r='marks', theta='Subjects', line_close=True)
        theory_fig.update_traces(fill='toself')
        st.write("Theory Marks Distribution")
        st.plotly_chart(theory_fig)
        term_work_fig = px.line_polar(term_work_df, r='marks', theta='Subjects', line_close=True)
        term_work_fig.update_traces(fill='toself')
        st.write("Term Work Marks Distribution")
        st.plotly_chart(term_work_fig)
    
    