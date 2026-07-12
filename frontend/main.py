import streamlit as st


navbar = st.navigation(
    {
        "Авторизация": [
            st.Page("authorization/login.py", title="Логин"),
            st.Page("authorization/registration.py", title="Регистрация"),
        ],
        "Главная":
    }
)
navbar.run()
