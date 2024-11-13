import pytest
from src.bank_account import BankAccount

def test_sum():
    a = 5
    b = 5
    assert a + b == 10

@pytest.mark.parametrize("amount, expected", [
    (100, 1100),
    (3000, 4000),
    (4500, 5500),
])
def test_deposit_multiple_amounts(amount, expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(amount)
    assert new_balance == expected