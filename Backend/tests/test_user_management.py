from unittest import TestCase

from user_management import UserManagement


class TestUserManagement(TestCase):
    def test_get_user_profile(self):
        manager = UserManagement()
        manager.add_user("user", "pass")
        print(manager.get_user_profile("user"))
        manager.db.delete_user("user")

    def test_hash_pass(self):

        manager = UserManagement()
        print(manager.hash_password("toll"))

    def test_user_add(self):

        manager = UserManagement()
        print(manager.add_user("admin", "admin"))