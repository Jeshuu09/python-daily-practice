# ATM System Using Abstraction

from abc import ABC, abstractmethod


class ATM(ABC):

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass


class MyATM(ATM):

    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Available Balance: Rs.", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Enter a valid amount!")


atm = MyATM(5000)

while True:

    print("\n===== ATM SYSTEM =====")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm.check_balance()

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)

    elif choice == "3":
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)

    elif choice == "4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice!")
