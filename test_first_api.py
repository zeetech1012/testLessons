from http.client import responses

import requests
from google.protobuf.unittest_custom_options_pb2 import required_enum_opt
from orca.speech import reset


class TestFirstApi:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "testUser"
        data = {'name': name}

        response = requests.get(url, params = data )

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no filed 'answer' in the response"
        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert expected_response_text == actual_response_text , "actual text in the response is not correct"