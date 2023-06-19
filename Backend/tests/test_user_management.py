from unittest import TestCase

from src.game.user_management import UserManagement


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

    def test_get_token_by_user(self):
        manager = UserManagement()
        status, token = manager.login("admin", "admins")
        token2 = manager.get_token_by_user("admin")
        print(token)
        print(token2)
        self.assertTrue(token == token2)

    def test_get_online_list(self):
        manager = UserManagement()
        status, token = manager.login("admin", "admins")
        status, token = manager.login("admina", "admins")
        token2 = manager.get_token_by_user("admin")
        print(manager.get_online_list())
