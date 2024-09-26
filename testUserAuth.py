from email.quoprimime import header_check
from http.client import responses

import requests
import pytest

class TestUserAuth:

    def test_auth_user(self):
        data = {"username":"superadmin","password":"supersuper"}

#авторизация и получение токена в СВИ
        response1 = requests.post('http://192.168.15.200:30322/api/v2/incidents/auth/login', data   = data )


        assert response1.status_code == 200
        assert "access_token" in response1.json() , "here is no bearer token "







