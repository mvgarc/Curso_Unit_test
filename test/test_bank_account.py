import unittest , os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from unittest.mock import patch
from exceptions import InsufficientFundsError , WithdrawalTimeRestrictionError
from bank_account import BankAccount

class BankAccountTests (unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance,1500 , "El balance no es igual")

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")
    
    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue (os.path.exists("transaction_log.txt"))

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        print (new_balance)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_raises_during_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)