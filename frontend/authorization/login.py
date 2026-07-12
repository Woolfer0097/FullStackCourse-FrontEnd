import streamlit as st
from streamlit import session_state
from session import user
from api.client import login


st.set_page_config(page_title="Логин")


with st.form("login_form", border=True):
    f"# Введите логин и пароль"
    st.subheader("Email")
    email = st.text_input("Email", value=session_state.get("login_form_email"), placeholder="Введите email...")

    st.subheader("Пароль")
    psw = st.text_input("Пароль", value=session_state.get("login_form_psw"), placeholder="Введите пароль...")

    if st.form_submit_button("Войти"):
        resp = login(email, psw)
        if resp.status_code == 200:
            user.save_access_token(resp)
        elif resp.status_code == 500:
            st.error("Внутренняя ошибка бэкенда")
            if st.secrets.get("log_level") == "DEBUG":
                st.error(resp.raw)
        else:
            st.error("Неправильный email или пароль")

