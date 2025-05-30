import streamlit as st


st.title('st.title(문자열) : 제목')
st.header('st.header(문자열) : 헤더')
st.subheader('st.subheader(문자열) : 부제헤더')
st.text('st.text(문자열) : 텍스트')

st.code('st.code(code) : 파이썬 코드 표시')

code = '''
    def hello():
        print("Hello Streamlit!!")
'''

st.code(code)

st.markdown('streamlit에서 **마크다운 사용 가능:sunglasses:')