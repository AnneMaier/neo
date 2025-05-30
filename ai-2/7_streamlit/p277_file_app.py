import streamlit as st
from io import BytesIO

st.title('스트림릿에서의 파일 사용 예')

uploaded_file = st.file_uploader('파일 업로드', type='txt')

if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data[:100])

uploaded_file = st.file_uploader('파일 업로드', type='png')

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data[:100])
    