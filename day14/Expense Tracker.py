# Expense Tracker

# Features:

# Add expense.
# Save to file.
# View all expenses.
# Calculate total spending.

expenses="Expenses.txt"

def add_expense():
    name=input("Enter Name of the Expense :")
    spend=input("Enter Spending of the Expense :")
    with open(expenses,"a") as file:
        file.write(f"{name},{spend}\n")

def  view_expenses():
    print("\n====Displaying All Expenses====")

    with open(expenses,"r") as file:
        expense=file.read()
    print(expense)

def total_spending():
    total=0

    with open(expenses,"r") as file:
        for expense in file:
            item,spend=expense.split(",")
            total+=float(spend)

    print("Total Spending is :",total)

def menu():
    print("\n ======Expense Tracker======\n")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Calculate total spending")
    print("4. Exit")

while True:
    menu()
    choice=int(input("Enter your Choice :"))
    if choice==1:
        add_expense()
    elif choice==2:
        view_expenses()
    elif choice==3:
        total_spending()
    elif choice==4:
        print("Thank You for choosing.")
        break
    else:
        print("Invalid Option")