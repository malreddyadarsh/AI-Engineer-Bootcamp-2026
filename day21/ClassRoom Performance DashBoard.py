# Classroom Performance Dashboard
# Features
# Load marks into NumPy arrays.
# Display statistics.
# Find toppers.
# Calculate class average.
# Show pass/fail counts.

import numpy as np
marks=np.array([
    [40,50,70],
    [50,60,45],
    [46,25,56],
    [23,40,35],
    [56,78,60],
    [90,43,65],
    [56,89,78],
    [78,71,51]
])

student_average=np.mean(marks,axis=1)
subject_average=np.mean(marks,axis=0)
highest_mark=np.max(marks)
lowest_mark=np.min(marks)
class_average=np.mean(student_average)


print(f"=====ClassRoom Performance DashBoard=====\n")
print(f"Total No.of Students :{len(marks)}")
print(f"Highest Marks is     :{highest_mark}")
print(f"Lowest Mark is       :{lowest_mark}")
print(f"\nStudent Averages :")

for i,avg in enumerate(student_average,start=1):
    print(f"Student {i+1}: {avg:.2f}")

print("\nSubject Averages :")

for i,avg in enumerate(subject_average,start=1):
    print(f"Subject {i+1}: {avg:.2f}")
topper = np.argmax(student_average)

print(f"\nTopper : Student {topper + 1}")
print(f"Topper Average : {student_average[topper]:.2f}")
print(f"\nClass Average is : {class_average:.2f}")
pass_count=np.sum(student_average >= 50)
fail_count=np.sum(student_average < 50)
print(f"\nPass Count is :{pass_count}")
print(f"\nFail Count is :{fail_count}")