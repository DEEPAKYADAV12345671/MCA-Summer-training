import random

# Base Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_number = self._generate_account_number()
        self.account_holder = account_holder
        self.balance = balance

    def _generate_account_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")

# SavingAccount Class
class SavingAccount(BankAccount):
    interest_rate = 0.04  # 4% fixed by bank

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied at rate {self.interest_rate * 100}%.")

# CurrentAccount Class
class CurrentAccount(BankAccount):
    overdraft_limit = 50000  # ₹50,000 fixed by bank

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Withdrawal denied. Overdraft limit exceeded.")

# Main Program
def main():
    print("Date: 13/8/2025")
    account_type = input("Enter account type (saving/current): ").strip().lower()
    name = input("Enter account holder name: ").strip()
    try:
        initial_balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Invalid balance amount.")
        return

    if account_type == "saving":
        account = SavingAccount(name, initial_balance)
        print("\nYour account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print(f"Interest Rate (Bank Fixed): {SavingAccount.interest_rate * 100}%")
    elif account_type == "current":
        account = CurrentAccount(name, initial_balance)
        print("\nYour account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print(f"Overdraft Limit (Bank Fixed): ₹{CurrentAccount.overdraft_limit}")
    else:
        print("Invalid account type.")
        return

    while True:
        print("\nChoose operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        if isinstance(account, SavingAccount):
            print("4. Apply Interest (Bank-decided rate)")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            account.display_balance()
        elif choice == "4" and isinstance(account, SavingAccount):
            account.apply_interest()
        elif choice == "5":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()