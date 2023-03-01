from unittest import TestCase

from persistenceapi import Persistence


class Testpersistence(TestCase):
    def test_load_user(self):
        per = Persistence()
        print(per.load_user("karl"))

    def test_user_creation(self):
        per = Persistence()
        per.create_user("cool-guy", "hahaha")
        user = per.load_user("cool-guy")
        per.delete_user("cool-guy")
        self.assertEqual("hahaha", user.password)

    def test_user_deletion(self):
        per = Persistence()
        per.create_user("awesome-guy", "hahaha")
        per.delete_user("awesome-guy")
        self.assertIsNone(per.load_user("awesome-guy"))
