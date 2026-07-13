# Student Management Syste
# 
# Features:
# 
# Add student.
# Update student.
# Display details.
# Calculate average marks.

class Student :
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    
    def display(self):
        print("\n=====Student Details=====\n")
        print("Student Name     :",self.name)
        print("Student Roll No. :",self.rollno)
        print("Student Marks    :",self.marks,"\n\n")

    def calculate_average(self):
        avg=sum(self.marks) / len(self.marks)
        print("\nAverage Marks is :",avg)
    
    def update(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
        print("\nStudent Details Updated Successfully.")
    
def menu():
    print("1. Display Student Details")
    print("2. Update Student")
    print("3. Calculate Average Marks")
    print("4. Exit")

def main():
    s=Student("Adarsh",31,[85,86,74])
    while True:
        menu()
        choice=input("Enter your choice :")
        if choice=="1":
            s.display()
        elif choice=="2":
            name=(input("Enter Student Name :"))
            rollno=int(input("Enter Roll Number :"))
            marks=[]
            for i in range(1,4):
                mark=int(input(f"Enter {i} marks :"))
                marks.append(mark)
            s.update(name,rollno,marks)
        elif choice=="3":
            s.calculate_average()
        elif choice=="4":
            print("Thank You for Choosing.")
            break
        else:
            print("Invalid Option.")
            
main()