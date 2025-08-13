class BankAccount:
    _next_account_number = 10001  

    def __init__(self, balance=0):
        self.account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

# Create accounts
account1 = BankAccount()
account2 = BankAccount(500)
print(f"Account 1 number: {account1.account_number}, Initial balance: {account1.get_balance()}")
print(f"Account 2 number: {account2.account_number}, Initial balance: {account2.get_balance()}")

account1.deposit(100)

account1.withdraw(50)
account1.withdraw(200) 
print(f"Current balance for account 1: {account1.get_balance()}")