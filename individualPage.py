import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


from data import create_database,fire_query
# Individual Analysis
def individualAnalysis(pd_df,filename):
    st.title("Individual Analysis")
    query = st.text_input('Enter a SQL Query:','select * from `Cleaned Marksheet`')
    create_database(filename,pd_df)
    individual_df = fire_query(query,filename)
    
    st.write(individual_df.T)
    
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

        temp = individual_df.values.T[1:]
        temp_df = pd.DataFrame(list(temp),columns=['Student Marks'])
        agg_df = calculateAgg(pd_df)
        df_merged = pd.concat([agg_df, temp_df], axis=1)
        
        for count,column in enumerate(pd_df):
            if count+1<len(pd_df.columns):
                fig = go.Figure(data=[go.Bar(x=list(df_merged.columns), y=list(df_merged.iloc[count]))])
                fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                                marker_line_width=1.5, opacity=0.6)
                fig.update_layout(title_text=pd_df.columns[count+1])
                st.plotly_chart(fig) 