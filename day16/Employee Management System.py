# Employee Management System
# 
# Features:
# 
# Add employee.
# Update salary.
# Display employee details.
# Search employee.

class Employee:
    def __init__(self,employee):
        self.employee=employee
    def add_employee(self):
        name=input("Enter Employee Name to add :")
        salary=int(input("Enter Employee Salary :"))
        emp={
            "name":name,
            "salary":salary
        }
        self.employee.append(emp)
        print("Employee Added Successfully.")

    def update_salary(self,name):
        if len(self.employee)==0:
            print("No Employees Added.")
        else:
            for emp in self.employee:
                if emp["name"]==name:
                    update_salary=int(input("Enter Salary to Update :"))
                    emp["salary"]=update_salary
                    print("Salary Updated Successfully.")
                    return
            print("No Employee Found To Update Salary.")   

    def display(self):
        if len(self.employee)==0:
            print("No Employee Details Found.")
        else:
            print("\n=====Displaying Employee Details=====\n")
            for emp in self.employee:
                print("Employee Name   :",emp["name"])
                print("Employee Salary :",emp["salary"])

    def search(self,name):
        if len(self.employee)==0:
            print("No Employee Details Found.")
        else:
            for emp in self.employee:
                if emp["name"]==name:
                    print("Employee Details Found.")
                    print("Employee Name :",emp["name"])
                    print("Employee Salary :",emp["salary"])
                    return
            print("No Employee Details Found.")
            
def menu():
    print("\n\n======Employee Management System======")
    print("1.Add employee")
    print("2. Update salary")
    print("3. Display employee details")
    print("4. Search employee")
    print("5. Exit")
                
def main():
    employee=[]
    emp=Employee(employee)
    while True:
        menu()
        choice=input("Enter your Choice :")
        if choice=="1":
            emp.add_employee()
        elif choice=="2":
            name=input("Enter Employee Name to Update Salary :")
            emp.update_salary(name)
        elif choice=="3":
            emp.display()
        elif choice=="4":
            name=input("Enter Employee Name to Search :")
            emp.search(name)
        elif choice=="5":
            print("Thank You for Choosing.")
            break
        else :
            print("Invalid Option.")

main()