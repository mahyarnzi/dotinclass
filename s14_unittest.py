import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(100, 99), 199)
        self.assertEqual(add(61, 5), 66)

    def test_subtract(self):
        self.assertEqual(subtract(10, 1), 9)
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(9, 5), 4)


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_deposit(self):
        self.account.deposit(20)
        self.assertEqual(self.account.balance, 120)

    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)



if __name__ == "__main__":
    unittest.main()
