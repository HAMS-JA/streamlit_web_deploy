import streamlit as st

st.set_page_config(
    page_icon="😆",
    page_title="행복한 현미닝의 웹",
    layout="wide",
)

st.subheader("반도체")

if st.button("Semi-conductor World"):
    st.write("버튼이 생성되었습니다")
else:
    st.write("버튼을 클릭해주세요.")
