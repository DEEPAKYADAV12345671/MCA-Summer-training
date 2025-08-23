import sys

class Bank:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient balance, withdrawal denied.")
        else:
            self.balance -= amount
        return self.balance

# Main program
name = input("Enter your name: ")
B = Bank(name)

while True:
    print('''
    Enter D to Deposit
    Enter W to Withdraw
    Enter E to Exit
    ''')
    choice = input("Enter your choice: ").strip().lower()

    if choice == "e":
        print("Thank you for banking with us!")
        sys.exit()

    try:
        amt = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        continue

    if choice == "d":
        print("Balance after deposit:", B.deposit(amt))
    elif choice == "w":
        print("Balance after withdrawal:", B.withdrawal(amt))
    else:
        print("Invalid choice. Please enter D, W, or E.")