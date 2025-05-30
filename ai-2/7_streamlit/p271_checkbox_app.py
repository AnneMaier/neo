import streamlit as st

st.title('스트림릿에서의 버튼 입력 사용 예')

checked1 = st.checkbox('Checkbox 1')
st.write('Checkbox 1 Status: ', checked1)

if checked1:
    st.write('checkbox 1 was checked')
else:
    st.write('checkbox 1 was not checked')

checked2 = st.checkbox('Checkbox 2')
st.write('Checkbox 2 Status: ', checked2)

if checked2:
    st.write('checkbox 2 was checked')
else:
    st.write('checkbox 2 was not checked')