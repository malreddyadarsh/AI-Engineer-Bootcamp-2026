# Features:

# Add student.
# Update details.
# Delete student.
# Search student.
# Display all students

students = {}

def add_student():
    sid = int(input("Enter Student ID: "))

    if sid in students:
        print("Student ID already exists.")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")

    students[sid] = {
        "name": name,
        "age": age,
        "branch": branch
    }

    print("Student added successfully!")


def display_students():

    if not students:
        print("No students found.")
        return

    print("\nStudent Records")

    for sid, details in students.items():
        print("----------------------")
        print("ID:", sid)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Branch:", details["branch"])


def search_student():

    sid = int(input("Enter Student ID: "))

    if sid in students:
        print("Student Found")
        print(students[sid])
    else:
        print("Student not found.")


def update_student():

    sid = int(input("Enter Student ID: "))

    if sid not in students:
        print("Student not found.")
        return

    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    branch = input("Enter New Branch: ")

    students[sid]["name"] = name
    students[sid]["age"] = age
    students[sid]["branch"] = branch

    print("Student updated successfully.")


def delete_student():

    sid = int(input("Enter Student ID: "))

    if sid in students:
        del students[sid]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")