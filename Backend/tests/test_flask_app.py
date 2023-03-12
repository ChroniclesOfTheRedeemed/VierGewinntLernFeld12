from unittest import TestCase

from src.flask_app import find_properties_in_answer


class Test(TestCase):
    def test_find_properties_in_answer(self):
        args = ["token", "username", "your_mother", "yikers"]
        json = {
            "token": "geoisfdkvnpserb",
            "username": "cool",
            "your_mother": 328409,
            "yikers": True
        }
        print(find_properties_in_answer(args, json))
        r = find_properties_in_answer(args, json)
        a, b, c, d = r
        print(a, b, c, d)


# class Test(TestCase):
#     def test_validate_request(self):
#         self.fail()
