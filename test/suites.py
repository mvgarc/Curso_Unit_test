import unittest

from test.test_bank_account import BankAccount

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccount("test_deposit"))
    suite.addTest(BankAccount("test_withdraw"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())