import streamlit as st
import pandas as pd
import subprocess
import webbrowser
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


def combinedAnalysis(pd_df):
    st.write(pd_df)
    sr_no = int(st.text_input('Enter the serial number associated with the student to view his/her details :','0'))
    #st.write(pd_df.loc[sr_no].to_frame().T)
    st.write(pd_df.loc[sr_no])
    

    df = pd.DataFrame(dict(
        r=[1, 5, 2, 2, 3],
        theta=['processing cost','mechanical properties','chemical stability',
            'thermal stability', 'device integration']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    #fig.show()
    st.plotly_chart(fig)
    categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[1, 5, 2, 2, 3],
        theta=categories,
        fill='toself',
        name='Product A'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[4, 3, 2.5, 1, 2],
        theta=categories,
        fill='toself',
        name='Product B'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 5]
        )),
    showlegend=False
    )

    fig.show()
    st.plotly_chart(fig)