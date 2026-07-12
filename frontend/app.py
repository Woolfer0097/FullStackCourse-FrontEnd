import streamlit as st


# Сюда нужно прописывать все новые страницы, которые вы создаёте
navbar = st.navigation(
    {
        "Авторизация": [
            st.Page("authorization/login.py", title="Логин"),
            st.Page("authorization/registration.py", title="Регистрация"),
        ] if st.session_state.get("access_token") is None
        else [
            st.Page("pages/profile.py", title="Профиль")
        ],
        "Основные страницы": [
            st.Page("pages/home.py", title="Главная"),
            st.Page("pages/container.py", title="Котики"),
            st.Page("pages/book1.py", title="доп страниц"),
        ]
    }
)
navbar.run()
