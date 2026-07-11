# Employee Database

# Features:

# Add employee.
# Update salary.
# Search employee.
# Delete employee.
# Display all employees.

employees={}

def add_employee(employees):
    id=input("Enter Employee ID :")
    if id in employees:
        print("Employee Details are already filled.")
        return
    name=input("Enter Employee Name :")
    salary=input("Enter Employee Salary :")
    employees[id]={
        "name":name,
        "salary":salary
    }
    print("Employee Details added successfully.")

def update_salary(employees):
    id=input("Enter Employee ID to Update Salary :")
    if id not in employees:
        print("No Employee Details found with the given ID.")
        return
    else:
        salary=input("Enter Employee Salary to Update :")
        employees[id]["salary"]=salary
        print("Employee Salary Updated Successfully.")

def search_employee(employees):
    id=input("Enter Employee ID to Search :")
    if id not in employees:
        print("No Employee Details found with the given ID.")
        return
    else:
        print("Employee Details Found.")
        print("Employee Id     :",id)
        print("Employee Name   :",employees[id]["name"])
        print("Employee Salary :",employees[id]["salary"])

def delete_employee(employees):
    id=input("Enter Employee ID to Search :")
    if id not in employees:
        print("No Employee Details found to Delete.")
        return
    
    del employees[id]
    print("Employee Deleted Successfully.")

def display(employees):
    if not employees:
        print("No Employees Found to Display.")
        return
    print("\n======Displaying Employee Details======")
    for id,details in employees.items():
        print("Employee Id     :",id)
        print("Employee Name   :",details["name"])
        print("Employee Salary :",details["salary"])
        print("----------------------------")

def menu():
    print("\n ===Employee Details===")
    print("1. Add employee")
    print("2. Update salary")
    print("3. Search employee")
    print("4. Delete employee")
    print("5. Display all employees")
    print("6. Exit")

while True:
    menu()
    choice=int(input("Enter your choice :"))
    if choice==1:
        add_employee(employees)
    elif choice==2:
        update_salary(employees)
    elif choice==3:
        search_employee(employees)
    elif choice==4:
        delete_employee(employees)
    elif choice==5:
        display(employees)
    elif choice==6:
        print("Thank you for Choosing ")
        break
    else:
        print("Invalid Option")

