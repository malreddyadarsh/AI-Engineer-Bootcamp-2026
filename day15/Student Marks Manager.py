# Student Marks Manager

# Features:

# Accept student details.
# Validate marks.
# Save valid records.
# Reject invalid entries with meaningful messages.

def add_student(students):
    try:
        name=input("Enter Student Name :").strip()
        
        if name=="":
            raise ValueError("Name cannot be empty.")
        
        roll_num=int(input("Enter Student Roll Number :"))

        marks=float(input("Enter Student's Marks :"))

        if marks<0 or marks>100:
            raise ValueError("Marks should be in between 0 and 100.")
        
        student={
            "Name":name,
            "Roll_number":roll_num,
            "Marks":marks
        }

        students.append(student)
        print("Student Added Successfully.")

    except ValueError as e :
        print("Error :",e)

def view_students(students):
    print("\n\nDisplaying All the students\n\n")

    if len(students)==0:
        print("No Students Found to Display.")
        return
    
    for student in students:
        print("Student Name :",student["Name"])
        print("Student Roll Number :",student["Roll_number"])
        print("Marks :",student["Marks"])
        print("-----------------------------------------")

def menu():
    print("\n\n======Student Marks Manager======")
    print("1. Adding Student Details.")
    print("2. Displaying Student Details")
    print("3. Exit ")

def main():
    students=[]
    
    while True:
        menu()
        choice=input("Enter your Choice :")
        if choice=="1":
            add_student(students)
        elif choice=='2':
            view_students(students)
        elif choice=='3':
            print("Thank You for Choosing.")
            break
        else:
            print("Invalid Option")

main()
