
class BankAccount:
    """
    Class for bank account with inital deposit of 0 if none     is give.
    """
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        """ Deposite method to deposite amount"""
        self.account_balance += amount

    def withdraw(self, amount):
        """ Withdrawal method for the class """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """ Display account method """
        print(f"Current Balance: ${self.account_balance:.2f}")
