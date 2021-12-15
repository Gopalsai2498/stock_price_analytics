# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 04:50:59 2021

@author: anil.ms
"""

import streamlit as st
from puts_page import show_puts_page
from calls_page import show_calls_page


st.sidebar.write('''
                 #### Developer: ####
                 ''')

st.sidebar.markdown('[![Anil-K MS]'
                    '(https://img.shields.io/badge/Author-Anil%20K%20MS-green)]'
                    '(https://www.linkedin.com/in/anil-kumar-m-1b136816a/)')


st.sidebar.write(''' ''')
                 
st.sidebar.write(''' ''')

st.sidebar.write(''' ''')
                 
st.sidebar.write(''' ''')
                 
st.sidebar.title('Calls/Puts')
page = st.sidebar.selectbox('select', ('calls', 'puts'))

if page=='calls':
    show_calls_page()
else:
    show_puts_page()