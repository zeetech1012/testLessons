import requests


class TestUserAuth:
    def test_auth_user(self):
        body = {
            "username":"superadmin",
                "password":"supersuper"
                }
        response1 = requests.post("http://192.168.15.200:30322/api/v2/incidents/auth/login", json=body )

        print(response1.status_code)
        assert response1.status_code == 200
        assert  "access_token" in response1.json()
        access_token_from_login = response1.json().get("access_token")




   

     response2  = requests.get(
            "http://192.168.15.200:30322/api/v2/incidents/auth/",
            headers={"authorization": access_token_from_login } ,

        )
        assert "token" in response2.json()
        token_from_check_method = response2.json()["token"]

        print(token_from_check_method)

        