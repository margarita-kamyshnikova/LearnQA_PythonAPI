from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserGet(BaseCase):
    def test_get_user_details_auth_as_not_the_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        response2 = MyRequests.get(
            "/user/1",
            headers = {"x-csrf-token": token},
            cookies = {"auth_sid": auth_sid}
            )

        Assertions.assert_json_has_key(response2, "username")
        Assertions.assert_json_has_not_key(response2, "email")
        Assertions.assert_json_has_not_key(response2, "firstName")
        Assertions.assert_json_has_not_key(response2, "lastName")