import streamlit as st


navbar = st.navigation(
    {
        "Авторизация": [
            st.Page("authorization/login.py", title="Логин"),
            st.Page("authorization/registration.py", title="Регистрация"),
        ],
        "Основные страницы": [
            st.Page("pages/main.py", title="Главная"),
            st.Page("pages/container.py", title="котики"),
        ]
    }
)
navbar.run()
