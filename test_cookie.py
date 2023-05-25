import requests

class TestCookie:
    def test_hw_cookie(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        assert response1.cookies == {'HomeWork': 'hw_value'}, f"There is another cookies"