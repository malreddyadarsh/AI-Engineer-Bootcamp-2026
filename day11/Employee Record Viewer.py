def display_employees(employees):
    print("======Employees Details=====")
    for emp in employees:
        print("\nEmployee ID :",emp[0],
              "\nEmployee Name :",emp[1],
              "\nEmployee Age :",emp[2],
              "\nEmployee Dept :",emp[3],
              "\nEmployee Salary :",emp[4])
        
def search_employee(employees):
    id=int(input("Enter employee id to search :"))

    for emp in employees:
        if emp[0]==id:
            print("=====Employee Details=====")
            print("\nEmployee ID :",emp[0],
              "\nEmployee Name :",emp[1],
              "\nEmployee Age :",emp[2],
              "\nEmployee Dept :",emp[3],
              "\nEmployee Salary :",emp[4])
            return
        
    print("Name Not Found ")

def department_info(employees):
    dept=input("Enter department name :").lower()
    found = False
    for emp in employees:
        if emp[3].lower()==dept:
            print("Employee Found in the dept :",dept)
            found=True
    
    if not found:
        print("No employee in the department")


def main():

    employees = (
        (101, "Adarsh", 22, "AI", 50000),
        (102, "Rahul", 25, "HR", 42000),
        (103, "Priya", 24, "Finance", 47000),
        (104, "Kiran", 27, "AI", 60000),
        (105, "Sneha", 23, "Marketing", 45000)
    )

    display_employees(employees)
    search_employee(employees)
    department_info(employees)


main()