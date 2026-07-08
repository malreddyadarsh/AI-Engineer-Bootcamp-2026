# Student Management System
 #Features:
   #  Add student details.
   #Calculate total, average, percentage.
   #Display grade.
   #Use functions for each task

def add_studetails():
    print("------Enter Student Details------")
    name=input("Enter student name :")
    roll=input("Enter student roll number :")
    marks=[]
    print("Enter 5 subject marks :")

    for i in range (1,6) :
        mark=0
        while True:
            mark=int(input(f"Enter {i}Subject marks:"))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Enter marks between 0 and 100 ")
    return(name,roll,marks)


def calculate(marks):
    total=sum(marks)
    avg=total/5
    perc=(total/500)*100
    return (total,avg,perc)


def calculate_grade(perc):
    if perc>=85:
        return 'A'
    elif perc<85 and perc>=75:
        return 'B' 
    elif perc<75 and perc>=50:
        return 'C'
    else:
        return 'Fail'
    

def display_result(name,roll,marks,total,avg,perc,grade):
    print("\n\n====== Student Report ======")
    print("Student Name :",name)
    print("Student Roll :",roll)

    print("Student's Mark List of 5 subjects:")
    for i in range(5):
        print("Subject", i + 1, "Marks :", marks[i])
    print("Total of 5 Subject Marks :",total)
    print("Average of marks         :",avg)
    print("Percentage of marks      :",perc)
    print("Grade                    :",grade)

def main():
    name,roll,marks=add_studetails()
    total,avg,perc=calculate(marks)
    grade=calculate_grade(perc)
    display_result(
        name,
        roll,
        marks,
        total,
        avg,
        perc,
        grade
    )

main()