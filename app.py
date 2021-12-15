# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 04:50:59 2021

@author: anil.ms
"""

import streamlit as st
from puts_page import show_puts_page
from calls_page import show_calls_page



page = st.sidebar.selectbox('Calls/Puts', ('calls', 'puts'))

if page=='calls':
    show_calls_page()
else:
    show_puts_page()