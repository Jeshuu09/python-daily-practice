# File-Based Expense Tracker

FILE_NAME = "expenses.txt"


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    if amount <= 0:
        print("Enter a valid amount!")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{amount}\n")

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses recorded.")
            return

        print("\n----- Expense Records -----")

        for expense in expenses:
            name, amount = expense.strip().split(",")
            print(f"{name}: Rs. {amount}")

    except FileNotFoundError:
        print("No expense records found.")


def calculate_total():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            for expense in file:
                name, amount = expense.strip().split(",")
                total += float(amount)

        print("Total Expenses: Rs.", round(total, 2))

    except FileNotFoundError:
        print("No expense records found.")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")
