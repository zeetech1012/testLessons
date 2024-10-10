from token import ASYNC

import requests
import pytest


from http.client import responses

import requests
from httplib2.auth import auth_param
from uaclient.files.user_config_file import user_config
from urllib3 import proxy_from_url


class TestUserAuth:
    def test_auth_user(self):
        body = {"username":"superadmin","password":"supersuper"}
        response1 = requests.post("http://192.168.15.200:30322/api/v2/incidents/auth/login", json=body )

        print(response1.status_code)
        assert response1.status_code == 200
        assert  "access_token" in response1.json()
        token = response1.json().get("access_token")




        response2  = requests.get(
            "http://192.168.15.200:30322/api/v2/incidents/auth/",
            headers={"authorization": token } ,

        )
        assert "token" in response2
        token_from_check_method = response2.json()["user_id"]

        print(token_from_check_method)

        assert token_from_check_method == token

