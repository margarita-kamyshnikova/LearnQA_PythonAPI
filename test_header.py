import requests

class TestHeader:
    def test_hw_cookie(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_header")
        head = response1.headers.get('x-secret-homework-header')
        assert response1.headers.get('x-secret-homework-header') == "Some secret value", f"There is no secret header"