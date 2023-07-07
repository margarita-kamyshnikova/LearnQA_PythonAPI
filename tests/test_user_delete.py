from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_user_delete(self):
        # (1) LOGIN WITH USER_ID 2
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234',
        }
        response = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id = self.get_json_value(response, "user_id")

        # (1) DELETE USER_ID 2
        response1 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response1, 400)
        assert response1.content.decode(
            "utf-8") == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", f"Unexpected response content {response1.content}"


        # (2) REGISTER WITH NEW USER
        register_data = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response2, "id")

        # (2) LOGIN WITH NEW USER
        login_data = {
            'email': email,
            'password': password,
        }
        response3 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # (2) DELETE NEW USER
        response4 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response4, 200)
        assert response4.content.decode(
            "utf-8") == f"", f"Unexpected response content {response4.content}"

        # (2) GET DELETED NEW USER
        response5 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response5, 404)
        assert response5.content.decode(
            "utf-8") == f"User not found", f"Unexpected response content {response5.content}"


        # (3) REGISTER WITH NEW USER
        register_data = self.prepare_registration_data()
        response6 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response6, 200)
        Assertions.assert_json_has_key(response6, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response6, "id")

        # (3) LOGIN WITH NEW USER
        login_data = {
            'email': email,
            'password': password,
        }
        response7 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response7, "auth_sid")
        token = self.get_header(response7, "x-csrf-token")

        # (3) DELETE ANOTHER USER
        response8 = MyRequests.delete(
            f"/user/2", # удаляю старого пользователя с токеном и куки нового пользователя
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response8, 200)
        assert response8.content.decode(
            "utf-8") == f"", f"Unexpected response content {response4.content}"


        # (3) GET USER WHOSE TOKEN AND COOKIE WERE USED

        response9 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response9, 404)
        assert response9.content.decode(
            "utf-8") == f"User not found", f"Unexpected response content {response9.content}"

