import requests

url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}

response = requests.get(url, headers=headers)

print(response.headers)
