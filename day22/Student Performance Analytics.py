# Student Performance Analytics
# 
# Build a console application that:
# 
# Generates or loads student marks.
# Displays:
# Class average.
# Subject average.
# Top scorer.
# Lowest scorer.
# Pass percentage.
# Filters students based on user-defined criteria.
# 
# Concepts Used:
# 
# NumPy arrays
# Boolean indexing
# Statistics
# Reshaping

import numpy as np
np.random.seed(42)

marks=np.random.randint(35,101,(10,3))
print("\nStudent Marks\n")
for i,mark in enumerate(marks,start=1):
    print(f"Student {i} :{mark}")

class_average=np.mean(marks)
print(f"\nClass Average is :{class_average:.2f}")

subject_averages=np.mean(marks,axis=0)
print("\nSubject Averages:\n")
for i,avg in enumerate(subject_averages,start=1):
    print(f"Subject {i} : {avg}")

student_averages=np.mean(marks,axis=1)
topper=np.max(student_averages)
topper_index=np.argmax(student_averages)
print(f"Topper Student {topper_index+1} : {topper}")

lowest=np.min(student_averages)
lowest_index=np.argmin(student_averages)
print(f"Lowest Student {lowest_index+1} : {lowest}")

passed=np.where(student_averages>=50)[0]
pass_percent=len(passed)/len(student_averages)*100
print(f"Pass Percentage is :{pass_percent:.2f}")

while True:
    print("-------------------------------------------")
    print("1 Above Average Students")
    print("2 Failed Students")
    print("3 Above 90 Marks")
    print("4 Exit")
    ch=int(input("\nEnter Your Choice:"))
    if ch==1:
        print("Above Average Students")
        above_average=np.where(student_averages > class_average)[0]
        if len(above_average)>0:
            for avg in above_average:
                print(f"Student {avg+1} : {student_averages[avg]:.2f}")
        else:
            print("No Students Above Class Average.")
    elif ch==2:
        failed=np.where(student_averages<50)[0]
        if len(failed)>0:
            print("\nFailed Students are :")
            for fail in failed:
                print(f"Student {fail} : {student_averages[fail]:.2f}")
        else:
            print("\nNo Failed Students.")
    elif ch==3:
        above_90=np.where(np.any(marks>90,axis=1))[0]
        if len(above_90)>0:
            print("Students Above 90 are :")
            for stu in above_90:
                print(f"Student {stu} : {marks[stu]}")
        else:
            print("\nNo Students Above 90 Marks")
    elif ch==4:
        print("Thank You for Choosing.")
        break
    else:
        print("Invalid Option.")
    