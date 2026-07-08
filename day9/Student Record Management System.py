def add_student(students):
    name=input("Enter student to be added :")
    students.append(name)
    return students

def update_student(students):
    name=input("Enter the name which you want to update :")
    if name in students:
        index=students.index(name)
        up_name=input("Enter the name to add :")
        students[index]=up_name
    return students

def delete_student(students):
    name=input("Enter the name you want to delete :")
    students.remove(name)
    return students

def search_student(students):
    name=input("Enter the name to search :")
    if name in students:
        print(name," is found in the students list.")

def display_all(students):
    print(students)

def menu():
    print("\n======Student Details======")
    print("1. Add student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display all Students")
    print("6. Exit")
def main():
    students=[]
    while True:
        menu()
        choice=int(input("Enter your choice :"))
        if choice==1:
            add_student(students)
        elif choice==2:
            update_student(students)
        elif choice==3:
            delete_student(students)
        elif choice==4:
            search_student(students)
        elif choice==5:
            display_all(students)
        elif choice==6:
            print("Thank you for choosing.")
            break
        else:
            print("Invalid option.")


main()