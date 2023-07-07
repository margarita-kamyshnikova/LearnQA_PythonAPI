from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_negative(self):

        # EDIT WITHOUT AUTHORIZATION
        new_name = "Changed Name"

        response = MyRequests.put(
            f"/user/2",
            data = {"firstName": new_name}
        )

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Auth token not supplied", f"Unexpected response content {response.content}"

        #EDIT WITH ANOTHER USER'S AUTHORIZATION

        # register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data = register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # login
        login_data = {
            'email': email,
            'password': password,
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # edit another user
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/1",
            headers = {"x-csrf-token": token},
            cookies = {"auth_sid": auth_sid},
            data = {"firstName": new_name}
        )

        #print(response3.content)
        Assertions.assert_code_status(response3, 200)
        #Проверить изменились ли данные у пользователя с id 1 я не могу, так как нет данных от его учетки. print отдает пустую строку.


        #EDIT SAME USER WITH NEW WRONG EMAIL
        new_wrong_email = "gud.maggiegmail.com"

        response4 = MyRequests.put(
            f"/user/{user_id}",
            headers = {"x-csrf-token": token},
            cookies = {"auth_sid": auth_sid},
            data = {"email": new_wrong_email}
        )

        Assertions.assert_code_status(response4, 400)
        assert response4.content.decode(
            "utf-8") == f"Invalid email format", f"Unexpected response content {response4.content}"


        #EDIT SAME USER WITH TOO SHORT FIRST NAME
        new_short_first_name = "g"

        response5 = MyRequests.put(
            f"/user/{user_id}",
            headers = {"x-csrf-token": token},
            cookies = {"auth_sid": auth_sid},
            data = {"firstName": new_short_first_name}
        )

        Assertions.assert_code_status(response5, 400)
        Assertions.assert_json_value_by_name(
            response5,
            "error",
            "Too short value for field firstName",
            "Unexpected response content"
        )







