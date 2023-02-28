from unittest import TestCase

from persistenceapi import Persistence


class Testpersistence(TestCase):
    def test_load_user(self):
        per = Persistence()
        print(per.load_user("karl"))
