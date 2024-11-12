import unittest , os
from faker import Faker

from src.user import User
from src.bank_account import BankAccount

class UserTests(unittest.TestCase):

    def setUp(self) -> None:
        self.faker = Faker(locale="es")
        self.user = User(name=self.faker.name(), email=self.faker.email())