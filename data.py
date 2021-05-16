import sqlite3
from sqlite3 import Connection
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

def create_database(filename,pd_df):
    engine = create_engine(f'sqlite:///{filename[0:len(filename)-5]}.db', echo=False)
    pd_df.to_sql(f'{filename[0:len(filename)-5]}',engine,if_exists='replace',index=False)


def fire_query(query,filename):
    con = sqlite3.connect(f'{filename[0:len(filename)-5]}.db')
    c = con.cursor()
    result=c.execute(query)
    names = list(map(lambda x: x[0], c.description))
    df=pd.DataFrame(result)
    df.columns=names
    return df







