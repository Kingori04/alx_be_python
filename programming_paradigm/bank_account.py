class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes the bank account with an optional initial balance.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if sufficient funds are available.
        Returns True if the withdrawal is successful, otherwise False.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
