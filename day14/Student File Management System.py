# Student File Management System

#Features:

# Add student.
# Save to file.
# View students.
# Search student.
# Delete student
file_s="students.txt"
def add_student():
    name=input("Enter student name to add:")
    with open(file_s,"a") as file:
        file.write(name + "\n")
    print("Student Name Added Successfully.")

def view_student():
    print("\n======Student Lists======\n")
    with open(file_s,"r") as file:
        students=file.read()
    print(students)

def search_student():
    name=input("Enter Student Name to Search :")
    found=False

    with open(file_s,"r") as file:
        for student in file:
            if student.strip().lower()==name.lower():
                found=True
                break
    
    if found:
        print("Student Name Found.")
    else:
        print("Student Name Not Found.")

def delete_student():
    name=input("Enter Student Name to Search :")

    with open(file_s,"r")as file:
        students=file.readlines()

    with open(file_s,"w") as file:
        found=False

        for student in students:
            if student.strip().lower()!=name.lower():
                file.write(student)
            else:
                found=True
        
        if found:
            print("Student Name Deleted Successfully.")
        else:
            print("Student Name Not Found to Delete.")

def menu():
    print("\n======Student File Management System======")
    print("1.Add Student ")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")

while True:
    menu()
    choice=int(input("Enter your choice :"))
    
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        search_student()
    elif choice==4:
        delete_student()
    elif choice==5:
        print("Thank you for choosing !")
        break
    else:
        print("Invalid Option")