import unittest
from src.bank_account import BankAccount

class BankAccountTests (unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)