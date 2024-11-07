import unittest
from src.bank_account import BankAccount

class BankAccountTests (unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500