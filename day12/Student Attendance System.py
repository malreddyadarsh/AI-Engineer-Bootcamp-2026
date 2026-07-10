attendance=set()

while True:
    print("\n\n=====Student Attendence System=====")
    print("1. Adding student names ")
    print("2. Check Attendence ")
    print("3. Display All Students ")
    print("4. Total no.of Students ")
    print("5. Exit ")

    choice=int(input("Enter your choice :"))
    if choice==1:
        name=input("Enter student name to add :")
        attendance.add(name)
        print("Student Name Added Successfully")
    elif choice==2:
        name=input("Enter Student Name to Check Attendence :")

        if name in attendance:
            print("Present")
        else:
            print("Absent")
    elif choice==3:
        if len(attendance)==0:
            print("There are no students, so pleade add students.")
        else:
            print("\n====Displaying All Students====")
            for student in attendance:
                print(student)
    elif choice==4:
        print("Total Unique Students:", len(attendance))
    elif choice==5:
        print("Thank you for choosing !")
        break
    else:
        print("Invalid Option , Please Choose correct option ! ")
