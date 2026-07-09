def add_student(students):
    name=input("Enter student name :").lower()
    for student in students:
        if student["name"]==name:
            print("Student name already exists.")
            return
    students.append({
        "name":name,
        "attendence":False
    })
    print("Student added successfully. ")
    return students

def mark_atten(students):
    name=input("Enter student name for marking attendence :").strip().lower()
    for student in students:
        if student['name']==name:
            student["attendence"]=True
            print("Attendence marked for ",student["name"])
            return
    print("Student name not found.")

def attendence_summary(students):
    print("\n======Attendence Summary======")
    present=0
    absent=0
    for student in students:
        if student["attendence"]==True:
            print(student['name'],"---->","1")
            present+=1
        else:
            print(student['name'],"---->","0")
            absent+=1
    
    print("Total students :",len(students))
    print("Present        :",present)
    print("Absent         :",absent)

def search_student(students):
    name=input("Enter student name for searching :").strip().lower()
    for student in students:
        if student["name"]==name:
            print("Student name found")
            return
    print("Student Name Not Found.")

def menu():
    print("\n Choose Below Options: ")
    print("1. Add student")
    print("2. Mark Attendence")
    print("3. Attendence Summary")
    print("4. Search Student")
    print("5. Exit ")

def main():
    students=[]
    while True:
        menu()
        ch=int(input("Enter your choice :"))
        if ch==1:
            add_student(students)
        elif ch==2:
            mark_atten(students)
        elif ch==3:
            attendence_summary(students)
        elif ch==4:
            search_student(students)
        elif ch==5:
            print("Thank you for choosing !")
            break
        else:
            print("Invalid Option")

main()