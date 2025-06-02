import streamlit as st
import pandas as pd
import time

file = st.file_uploader('CSV 파일 업로드', type=['csv','xlsx','xls'])

time.sleep(3)


if file is not None:
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        df = pd.read_csv(file)
    elif 'xls' in ext:
        df = pd.read_excel(file, engine='openpyxl')
        st.dataframe(df)
    
