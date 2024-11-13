import pytest
from src.bank_account import BankAccount

def test_sum():
    a = 5
    b = 5
    assert a + b == 10

def test_deposit_multiple_ammounts(self):
    test_cases = [
        {"ammount": 100, "expected": 1100},
        {"ammount": 3000, "expected": 4000},
        {"ammount": 4500, "expected": 5500},
    ]
    for case in test_cases:
        with self.subTest(case=case):
            self.account = BankAccount(balance=1000, log_file="transactions.txt")
            new_balance = self.account.deposit(case["ammount"])
            self.assertEqual(new_balance, case["expected"])