def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/etc.): ")

    expenses.append({
        "name": name,
        "amount": amount,
        "category": category
    })

    print("Expense added successfully.")


def display_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spending = ₹{total}")


def highest_expense(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\nHighest Expense")
    print("Name     :", highest["name"])
    print("Amount   :", highest["amount"])
    print("Category :", highest["category"])


def filter_category(expenses):
    category = input("Enter category: ").lower()

    found = False

    print(f"\nExpenses in '{category}' category:\n")

    for expense in expenses:
        if expense["category"].lower() == category:
            print(f"{expense['name']} - ₹{expense['amount']}")
            found = True

    if not found:
        print("No expenses found in this category.")


def display_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n====== Expense List ======")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']} ({expense['category']})")


def menu():
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. Display All Expenses")
    print("3. Display Total Spending")
    print("4. Show Highest Expense")
    print("5. Filter by Category")
    print("6. Exit")


def main():
    expenses = []

    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_expense(expenses)

        elif choice == 2:
            display_expenses(expenses)

        elif choice == 3:
            display_total(expenses)

        elif choice == 4:
            highest_expense(expenses)

        elif choice == 5:
            filter_category(expenses)

        elif choice == 6:
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()