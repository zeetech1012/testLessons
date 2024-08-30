import requests

'''
payload = {"name":"User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)

print(response.text)

response = requests.get("https://playground.learnqa.ru/api/hello", params = {"name", "user"})
parsed_response_text = response.json()
print(parsed_response_text["answer"])
'''

'''
response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")
'''

#урок 7 параметры запросов
''' 
response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1":"value1"})
--- для гет запросос параметры

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
--- для остальных передает дату (хотя видимо в новой версси можно везде парам )

print(response.text) 
'''

#урок 8 коды ответов
'''
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
seconde_response = response
print(first_response.url)
print(seconde_response.url)
print(response.text) 
'''

#  урок 9 хэдэры
'''
headers = {"some_header":"123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers )

print(response.text)
print((response.headers)) 
'''

#10 lesson Cookie
'''
payload = {"login": "secret_login", "password": "secret_pass"}

response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get('auth_cookie')

cookies = {'auth_cookie': cookie_value}

response2 = requests.post("https://playground.learnqa.ru/api/chek_auth_cookie", cookies=cookies)

print(response2.text) '''









