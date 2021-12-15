# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 04:55:55 2021

@author: anil.ms
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly 
import plotly.express as px
import plotly.graph_objects as go

def data_load():
    
    return df

#call_df
def data_load():
    data = pd.read_csv(r'final_df.csv')
    
    data['expiry_dt'] = pd.to_datetime(data['expiry_dt'])
    
    return data

df = data_load()

def show_calls_page():
    st.title('calls information')
            
    symbols = ['AARTIIND', 'ABBOTINDIA', 'ABFRL']
    
    expiry_date = ['2021-11-25T00:00:00.000000000']
    
    strike_price = [1000.0,  1100.0,  1150.0,  1200.0, 21000.0, 23000.0,   250.0,   255.0, 260.0, 280.0,   290.0,   300.0]
    
    symbols = st.selectbox('symbols', symbols)
    
    expiry_date = st.selectbox('expiry date', expiry_date)
    
    strike_price = st.selectbox('strike price', strike_price)
    
    ok = st.button('submit')
    
    df = data_load()
    
    if ok:
        ##sym = symbols
        #exp_dt = expiry_date
        #str_pr = strike_price
        
        df = df[(df['symbol']==symbols) & (df['expiry_dt']==expiry_date) & (df['strike_pr']==strike_price)]
        
        st.write(df.head())
        
        st.write("""### fetching data with increasing trend of Open interest""")
        
        data = df[['timestamp', 'open_int']]
        
        data['date'] = pd.to_datetime(data['timestamp']).dt.strftime('%Y %b %d')
        
        #fig = px.line(data)
        
        fig = px.line(data, x="date", y="open_int", title='open int', )
        
        st.write(fig)
        
        
        #print(data)        
        #fig, ax = plt.subplots()
        #plt.figure(figsize=(12,8))
        
        #st.line_chart(data)
        
        
        
        
        
        #confirmed
        


