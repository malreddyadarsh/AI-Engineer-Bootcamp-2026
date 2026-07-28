# Project 3 – Employee Payroll System
# 
# Features:
# 
# Different employee roles.
# Salary calculation.
# Method overriding for bonus calculation.

class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def display_details(self):
        print("Employee Role  :",type(self).__name__)
        print(f"Employee Name :{self.name}")
        print(f"Employee ID   :{self.emp_id}")
        print(f"Salary        :{self.salary}")

    def calculate_bonus(self):
        return 0
    
class Manager(Employee):
    def __init__(self,emp_id,name,salary):
        super().__init__(emp_id,name,salary)

    # Manager Receives 20% Bonus
    def calculate_bonus(self):
        return self.salary*0.20
  
    def display_details(self):
        super().display_details()
        bonus=self.calculate_bonus()
        print("Bonus Received is :",bonus)
        print("Total Salary is   :",bonus+self.salary)
        print("-"*30)

class Developer(Employee):
    def __init__(self,emp_id,name,salary):
        super().__init__(emp_id,name,salary)

    # Developer Receives 10% Bonus
    def calculate_bonus(self):
        return self.salary*0.10

    def display_details(self):
        super().display_details()
        bonus=self.calculate_bonus()
        print("Bonus Received is :",bonus)
        print("Total Salary is   :",bonus+self.salary)
        print("-"*30)

class Intern(Employee):
    def __init__(self,emp_id,name,salary):
        super().__init__(emp_id,name,salary)


    # Intern Receives 5% Bonus
    def calculate_bonus(self):
        return self.salary*0.05


    def display_details(self):
        super().display_details()
        bonus=self.calculate_bonus()
        print("Bonus Received is :",bonus)
        print("Total Salary is   :",bonus+self.salary)
        print("-"*30)

manager=Manager("10","Adarsh Reddy",110000)
developer=Developer("101","Rahul",75000)
intern=Intern("201","Govardhan",50000)
              
employees=[manager,developer,intern]

for emp in employees:
    emp.display_details()