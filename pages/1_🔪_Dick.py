import streamlit as st

st.set_page_config(
    page_icon="😆",
    page_title="행복한 현미닝의 웹",
    layout="wide",
)

st.subheader("Play")

if st.button("MOSFET 실행하기"):
    st.write("Good")
else:
    st.button("BJT 실행하기")

