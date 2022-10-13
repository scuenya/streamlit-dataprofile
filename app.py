import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

import sys
import os

st.set_page_config(page_title='Data Profiling',layout='wide')

def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext in  ('.csv', '.xlsx'):
        return ext
    else:
        return False


with st.sidebar:
        st.write('Modes of Operations')
        minimal = st.checkbox('Do you want it Minimal?')
        color = st.radio('Choose the option', options=('Primary','Dark','Orange')) 
        if color == 'Dark':
            dark_mode = True
            orange_mode = False
        elif color == "Orange":
            dark_mode = False
            orange_mode = True
        else:
            dark_mode = False
            orange_mode = False
           
        uploaded_file = st.file_uploader('Upload .csv, .xls files not exceeding 10mb')

if uploaded_file is not None:
    ext = validate_file(uploaded_file)
    st.write(ext)
    if ext:
        if ext == '.csv':
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head()) 
        elif ext == '.xlsx':
            xl_file = pd.ExcelFile(uploaded_file)
            sheet_tuple = tuple(xl_file.sheet_names)
            sheet_name = st.sidebar.selectbox('Select the sheet', sheet_tuple)
            df = xl_file.parse(sheet_name)
        else:
            st.error('ADENTRO kindly upload xls file or csv file') 

        with st.spinner('Generating Report'):
            pr = ProfileReport(df,minimal=minimal,dark_mode=dark_mode,orange_mode= orange_mode )
        st_profile_report(pr)
    else:
        st.error('kindly upload xls file or csv file') 
      
   
            