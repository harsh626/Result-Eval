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

    # subjects = ['Applied-Mathematics I', 'Engineering Physics I' , 'Engineering Chemistry I' , 'Engineering Mechanics' , 'Basic Electrical Engineering']
    # y = pd_df[sr_no]['Applied-Mathematics I']

    # fig = go.Figure([go.Bar(x=subjects, y=y)])
    
    # st.plotly_chart(fig)

    # df = pd.DataFrame(dict(
    #     r=[1, 5, 2, 2, 3],
    #     theta=['processing cost','mechanical properties','chemical stability',
    #         'thermal stability', 'device integration']))

    # fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    # fig.update_traces(fill='toself')
    # st.plotly_chart(fig)


    # categories = ['processing cost','mechanical properties','chemical stability',
    #           'thermal stability', 'device integration']

    # fig = go.Figure()

    # fig.add_trace(go.Scatterpolar(
    #     r=[1, 5, 2, 2, 3],
    #     theta=categories,
    #     fill='toself',
    #     name='Product A'
    # ))
    # fig.add_trace(go.Scatterpolar(
    #     r=[4, 3, 2.5, 1, 2],
    #     theta=categories,
    #     fill='toself',
    #     name='Product B'
    # ))

    # fig.update_layout(
    # polar=dict(
    #     radialaxis=dict(
    #     visible=True,
    #     range=[0, 5]
    #     )),
    # showlegend=False
    # )

    # st.plotly_chart(fig)

    df = pd_df

    Pass, Fail = 0, 0
    for i in range(130):
        if df['PassFail'][i] == 0:
            Fail += 1
        else:
            Pass += 1

    st.title("Passing and failing percentage")

    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

    fig = px.pie(df, labels=['Pass','Fail'], names='PassFail')
    
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                    marker=dict(colors=colors, line=dict(color='#000000', width=2)))

    st.plotly_chart(fig)