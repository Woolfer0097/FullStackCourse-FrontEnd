import streamlit as st
from streamlit import session_state
from api.client import register, login
from session import user


st.set_page_config(page_title="Логин")


with st.form("registration_form", border=True):
    f"# Введите логин и пароль"
    st.subheader("ФИО")
    fio = st.text_input("Полное имя", key="registration_form_full_name", value=session_state.get("full_name"), placeholder="Введите ФИО...")
    session_state["full_name"] = fio

    st.subheader("Email")
    email = st.text_input("Логин", key="registration_form_email", value=session_state.get("email"), placeholder="Введите почту...")
    session_state["email"] = email

    st.subheader("Пароль")
    psw = st.text_input("Пароль", key="registration_form_psw", value=session_state.get("psw"), placeholder="Введите пароль...")

    st.subheader("Введите пароль ещё раз")
    psw_repeat = st.text_input("Пароль", key="registration_form_repeat_psw", value=session_state.get("psw"), placeholder="Введите пароль...")

    submitted = st.form_submit_button("Регистрация", key="registration_form_registration_btn_submit")
    if submitted:
        if psw_repeat != psw:
            st.error("Пароли не совпадают!")
        else:
            resp = register(email, psw, fio)
            if resp.status_code == 201:
                resp = login(email, psw)
                print(resp.raw)
                if resp.status_code == 200:
                    user.save_access_token(resp.json())
                    st.switch_page("pages/home.py")
                else:
                    st.error("Ошибка!")
            elif resp.status_code == 500:
                st.error("Внутренняя ошибка бэкенда")
                if st.secrets.get("log_level") == "DEBUG":
                    st.error(resp.raw)
            else:
                st.error("Неправильный email или пароль")
                st.error(resp.text)
