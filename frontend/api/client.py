import requests
import json

BACKEND_URL = "http://127.0.0.1:8000"

LOGIN_ENDPOINT = f"{BACKEND_URL}/auth/login/"
REGISTER_ENDPOINT = f"{BACKEND_URL}/auth/register/"


def register():
    data = {
      "email": "string1@email.com",
      "password": "s1234535",
      "full_name": "Danila"
    }
    response = requests.post(REGISTER_ENDPOINT, json=data) # , headers={"Authorization": f"Bearer {token}"}
    print(response.json())


if __name__ == '__main__':
    register()
