# Daily Expense Tracker

expenses = []

while True:
    expense = input("Enter expense name (or 'done' to finish): ")

    if expense.lower() == "done":
        break

    amount = float(input("Enter expense amount: "))

    expenses.append((expense, amount))

print("\n----- Expense Summary -----")

total = 0

for name, amount in expenses:
    print(name, ":", amount)
    total += amount

print("--------------------------")
print("Total Expenses:", total)
