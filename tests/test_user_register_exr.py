from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest

class TestUserRegister(BaseCase):

   # НЕТ @ в email
    def test_create_without_add_symbol(self):
        data = {
            'email': 'gud.maggiegmail.com',
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa'
        }

        response = MyRequests.post("/user/", data=data)

        index = data['email'].find("@")

        Assertions.assert_code_status(response, 400)
        assert index == -1 , f"Invalid email format"

    # НЕТ ОДНОГО ИЗ ПОЛЕЙ
    fields = [
        {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa','lastName': 'learnqa'},
        {'email': 'gud.maggie@gmail.com', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'},
        {'email': 'gud.maggie@gmail.com', 'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa'},
        {'email': 'gud.maggie@gmail.com', 'password': '123', 'username': 'learnqa', 'lastName': 'learnqa'},
        {'email': 'gud.maggie@gmail.com', 'password': '123', 'username': 'learnqa', 'firstName': 'learnqa'}
    ]

    @pytest.mark.parametrize('condition', fields)

    def test_create_without_some_field(self, condition):
        data = condition
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert "email", f"The following required params are missed: email"
        assert "username", f"The following required params are missed: username"
        assert "firstName", f"The following required params are missed: firstName"
        assert "lastName", f"The following required params are missed: lastName"
        assert "password", f"The following required params are missed: password"


    # ИМЯ ИЗ 1 СИМВОЛА
    def test_very_short_firstname(self):
        data = {
            'email': 'gud.maggie1@gmail.com',
            'password': '123',
            'username': 'learnqa',
            'firstName': 'l',
            'lastName': 'learnqa'
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert len(data['firstName']) <= 1, f"Your first name must contain more than 1 character"

    # ИМЯ ИЗ 250 СИМВОЛОВ
    def test_very_long_firstname(self):
        data = {
            'email': 'gud.maggie1@gmail.com',
            'password': '123',
            'username': 'learnqa',
            'firstName': 'Текст можно проверить сразу полностью или вводить по строке, если нужен более качественный анализ. В любом случае онлайн-подсчет количества символов будет точным и быстрым, ведь скорость работы программы зависит только от возможности вашего подключения к интернету.',
            'lastName': 'learnqa'
            }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert len(data['firstName']) > 250, f"Your first name must contain lesser than 250 characters"









