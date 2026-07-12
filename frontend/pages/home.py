import streamlit as st

"# Главная"

token = st.session_state.get("access_token")
if token is not None:
    st.write("Ваш токен", token)
