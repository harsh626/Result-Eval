import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from data import create_database,fire_query

# file Uploading Funtion
#def uploadFile():
#    uploaded_file = None
#    uploaded_file = st.text_input('Enter a file path:','xyz.xlsx')
#    return uploaded_file

def uploadFile():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        return uploaded_file.name

# Cleaning Funtion
def cleaning(uploaded_file):
    df = pd.read_excel(uploaded_file)
    # Applied Mathematics Theory
    AM_1_list = []
    for i in range(0,130):
        AM_1_list.append(df._get_value(i,'AM - 1'))
    AM_1_list

    # Engineering Physics Theory
    EP_1_list = []
    for i in range(0,130):
        EP_1_list.append(df._get_value(i,'EP - 1'))
    EP_1_list

    #Engineering Chemistry Theory
    EC_1_list = []
    for i in range(0,130):
        EC_1_list.append(df._get_value(i,'EC - 1'))
    EC_1_list

    #Engineering Mechanics
    EM_1_list = []
    for i in range(0,130):
        EM_1_list.append(df._get_value(i,'EM'))
    EM_1_list


    #Basic Electrical Engineering
    BEE_1_list = []
    for i in range(0,130):
        BEE_1_list.append(df._get_value(i,'BEE'))
    BEE_1_list


    #Applied Mathematics Term Work
    AM_1_TW_list = []
    for i in range(0,130):
        AM_1_TW_list.append(df._get_value(i,'AM - 1 TW'))
    AM_1_TW_list


    #Engineering Physics 1 Term Work
    EP_1_TW_list = []
    for i in range(0,130):
        EP_1_TW_list.append(df._get_value(i,'EP - 1 TW'))
    EP_1_TW_list


    #Engineering Chemistry 1 Term Work
    EC_1_TW_list = []
    for i in range(0,130):
        EC_1_TW_list.append(df._get_value(i,'EC - 1 TW'))
    EC_1_TW_list


    #Engineering Mechanics Term Work
    EM_TW_list = []
    for i in range(0,130):
        EM_TW_list.append(df._get_value(i,'EM TW'))
    EM_TW_list


    #Basic Electrical Engineering Term Work
    BEE_TW_list = []
    for i in range(0,130):
        BEE_TW_list.append(df._get_value(i,'BEE TW'))
    BEE_TW_list


    #Workshop
    Workshop_list = []
    for i in range(0,130):
        Workshop_list.append(df._get_value(i,'WORKSHOP'))
    Workshop_list


    #G.P.A
    GPA_list = []
    for i in range(0,130):
        GPA_list.append(df._get_value(i,'GPA'))
    GPA_list

    #Names
    Names_list = []
    for i in range(130):
        Names_list.append(df._get_value(i,'NAME'))

    # Creating Dataframe
    pd_df = pd.DataFrame(list(zip(
        Names_list   ,
        AM_1_list ,
        EP_1_list ,
        EC_1_list ,
        EM_1_list ,
        BEE_1_list ,
        Workshop_list ,
        GPA_list        ,
        AM_1_TW_list        ,
        EP_1_TW_list        ,
        EM_TW_list        ,
        BEE_TW_list       ,
        EC_1_TW_list )),
        columns =['Names', 'Applied-Mathematics I' , 'Engineering Physics I' , 'Engineering Chemistry I' , 'Engineering Mechanics' , 'Basic Electrical Engineering' , 'Workshop','G.P.A','Applied Mathematics Term Work','Engineering Physics Term Work','Engineering Mechanics Term Work','BEE Term Work','Engineering Chemistry Term Work'])

    return pd_df


def passfail(uploaded_file):
    df = pd.read_excel(uploaded_file)
    PassFail_list = []
    for i in range(130):
        PassFail_list.append(int(df._get_value(i,'PASS_FAIL')))

    pa_df = pd.DataFrame(list(zip(
        PassFail_list
         )),
        columns =['PassFail'])
    return pa_df


# Combined Analysis Funtion
def combinedAnalysis(pd_df,pa_df):
    st.write(pd_df)
    #Jugaad
    st.title("Passing and failing percentage")
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
    fig = px.pie(pa_df, labels=['Pass','Fail'], names='PassFail')
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                    marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    st.plotly_chart(fig)


    #Bar Graphs
    agg_df = calculateAgg(pd_df)
    for count,column in enumerate(pd_df):
        if count+1<len(pd_df.columns):
            fig = go.Figure(data=[go.Bar(x=list(agg_df.columns), y=list(agg_df.iloc[count]))])
            fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                            marker_line_width=1.5, opacity=0.6)
            fig.update_layout(title_text=pd_df.columns[count+1])
            st.plotly_chart(fig)

    number = int(st.text_input("Enter the number of top records to be displayed: "))
    option = str(st.selectbox(
    'Enter Subject to be selected',
    ('Applied-Mathematics I' , 'Engineering Physics I' , 'Engineering Chemistry I' , 
     'Engineering Mechanics' ,'Basic Electrical Engineering' , 'Workshop','G.P.A',
     'Applied Mathematics Term Work','Engineering Physics Term Work',
     'Engineering Mechanics Term Work','BEE Term Work','Engineering Chemistry Term Work')))

    pd_df.sort_values(by=option, inplace=True, ascending = False)
    sorted_list =  pd_df[option][0:number]
    names_list = pd_df['Names'][0:number]
    sorted_df = pd.DataFrame(
        list(zip(
            names_list,
            sorted_list
        )),
        columns = ['Names',option])
    st.write(sorted_df)

def calculateAgg(pd_df):
    avg_list=[]
    max_list=[]
    min_list=[]
    for count,column in enumerate(pd_df.columns):
        if count==0:
            pass
        else:
            max_list.append(pd_df[column].max())
            avg_list.append(pd_df[column].mean())
            min_list.append(pd_df[column].min())
    
    agg_df = pd.DataFrame(list(zip(
    max_list,
    avg_list,
    min_list
        )),
        columns =['Maximum','Average','Minimum'])
    return agg_df


    
# Individual Analysis

def individualAnalysis(pd_df,uploaded_file):
    st.title("Individual Analysis")
    Name = st.text_input('Enter a Name')
    query = 'select*from `Cleaned Marksheet` where Names='+Name
    create_database(uploaded_file,pd_df)
    individual_df = fire_query(query,uploaded_file)
    
    st.write(individual_df)
    
    

    #radar graph
    if len(individual_df)==1:
        theory_df = pd.DataFrame(dict(
            marks=individual_df.values[0][1:7],
            Subjects=individual_df.columns[1:7]))
        term_work_df = pd.DataFrame(dict(
            marks=individual_df.values[0][8:],
            Subjects=individual_df.columns[8:]))

        AMP = []
        EPP = []
        ECP = []
        EMP = []
        BEEP = []
        WP = []
        AMTWP = []
        EPTWP = []
        ECTWP = []
        EMTWP = []
        BEETWP = [] 
        for column in individual_df.columns:
            if column=='Applied-Mathematics I':
                for value in list(individual_df[column]):
                    AMP.append((value/100)*100)
            elif column=='Engineering Physics I':
                for value in list(individual_df[column]):
                    EPP.append((value/75)*100)
            elif column=='Engineering Chemistry I':
                for value in list(individual_df[column]):
                    ECP.append((value/75)*100)
            elif column=='Engineering Mechanics':
                for value in list(individual_df[column]):
                    EMP.append((value/100)*100)
            elif column=='Basic Electrical Engineering':
                for value in list(individual_df[column]):
                    BEEP.append((value/100)*100)
            elif column=='Workshop':
                for value in list(individual_df[column]):
                    WP.append((value/50)*100)
            elif column=='Applied Mathematics Term Work':
                for value in list(individual_df[column]):
                    AMTWP.append((value/25)*100)

            elif column=='Engineering Physics Term Work':
                for value in list(individual_df[column]):
                    EPTWP.append((value/25)*100)
        
            elif column=='Engineering Mechanics Term Work':
                for value in list(individual_df[column]):
                    EMTWP.append((value/50)*100)

            elif column=='BEE Term Work':
                for value in list(individual_df[column]):
                    BEETWP.append((value/50)*100)
            elif column=='Engineering Chemistry Term Work':
                for value in list(individual_df[column]):
                    ECTWP.append((value/25)*100)

        theory_percent_df_temp = pd.DataFrame(list(zip(
        AMP,
        EPP,
        ECP,
        EMP,
        BEEP,
        WP)),
        columns =['Applied-Mathematics I' , 'Engineering Physics I' , 
        'Engineering Chemistry I' , 'Engineering Mechanics' , 'Basic Electrical Engineering' ,
         'Workshop'])

        theory_percent_df = pd.DataFrame(dict(
            marks=theory_percent_df_temp.values[0][0:],
            Subjects=theory_percent_df_temp.columns[0:]))
        

        practical_percent_df_temp  = pd.DataFrame(list(zip(
        AMTWP,
        EPTWP,
        EMTWP,
        BEETWP,
        ECTWP)),
        columns =['Applied Mathematics Term Work','Engineering Physics Term Work',
         'Engineering Mechanics Term Work','BEE Term Work','Engineering Chemistry Term Work'])

        practical_percent_df = pd.DataFrame(dict(
            marks=practical_percent_df_temp.values[0][0:],
            Subjects=practical_percent_df_temp.columns[0:]))

        theory_percent_fig = px.line_polar(theory_percent_df, r='marks', theta='Subjects', line_close=True,range_r=[0,100.00])
        theory_percent_fig.update_traces(fill='toself')

        st.write("Theory Marks Distribution")

        st.plotly_chart(theory_percent_fig)

        practical_percent_fig = px.line_polar(practical_percent_df, r='marks', theta='Subjects', line_close=True,range_r=[0,100.00])
        practical_percent_fig.update_traces(fill='toself')

        st.write("Term Work Marks Distribution")
        st.plotly_chart(practical_percent_fig)

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




