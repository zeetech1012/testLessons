import json.decoder
from http.client import responses

from pkg_resources.extern import names
from requests import Response


# noinspection PyUnreachableCode
class BaseCase:
    def get_cookie(self, resposne: Response, cookie_name):
        assert cookie_name in response.cookies , f"cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.header, f"Cannot find header with the name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict =response.json()
        except json.decoder.JSONDecoderError:
            assert  False , f"Response is not json. Response test '{response.text}' "

        assert  name in response_as_dict , f"Repsponse json dosnt have key '{name}'"

        return response_as_dict[name]