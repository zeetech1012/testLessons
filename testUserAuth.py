from http.client import responses

import requests
from httplib2.auth import auth_param
from uaclient.files.user_config_file import user_config


class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password':'123'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data = data )

        assert  "auth_sid" in response1.cookies , "no cookie"
        assert  "x-csrf-token" in response1.headers ,  "no headers"
        assert "user_id" in response1.json() , "no user"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]

        response2  = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": token} ,
            cookies={"auth_sid":auth_sid}
        )
assert "user_id" in response2.json(), "no user in 2nd response "
user_id_from_check_method = response2.json()["user_id"]
print(user_id_from_check_method)

assert user_id_from_check_method == user_id_from_check_method

