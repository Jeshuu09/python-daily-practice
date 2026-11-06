# Personal Banking System

balance = 1000
transactions = []

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: Rs.", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            transactions.append("Deposited Rs. " + str(amount))
            print("Money deposited successfully!")
        else:
            print("Enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount.")
        elif amount <= balance:
            balance -= amount
            transactions.append("Withdrawn Rs. " + str(amount))
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("\n----- Transaction History -----")

        if not transactions:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(transaction)

    elif choice == "5":
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice. Please try again.")
