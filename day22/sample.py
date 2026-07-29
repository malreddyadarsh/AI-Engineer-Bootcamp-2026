# # Program 1 
# # Reshape & Flatten
# # 
# # Create a 1D array.
# # 
# # Perform:
# # 
# # reshape()
# # flatten()
# # ravel()
# # 
# # Print each result.
# 
# import numpy as np
# arr=np.arange(9).reshape(3,3)
# print(arr)
# # Using Flatten()
# flat=arr.flatten()
# print(flat)
# flat[0]=10
# print("Array Using Flatten :",flat)
# print("Original Array :\n",arr)
# 
# # Using Ravel()
# ar=arr.ravel()
# print(ar)
# ar[0]=10
# print("Original Array is :",arr)
# print("Array using ravel :\n",ar)


# # Program 2 – Student Filter
# 
# # Given:
# 
# # marks = np.array([55,76,32,89,95,41,60])
# 
# # Display:
# 
# # Passed students.
# # Failed students.
# # Students scoring above 80.
# 
# import numpy as np
# marks = np.array([55,76,32,89,95,41,60])
# passed=np.where(marks>=50)[0]
# print("Passed Students :")
# for i in passed:
    # print(f"Student {i+1} : {marks[i]}")
# 
# failed=np.where(marks<50)[0]
# print("Failed Students :")
# for i in failed :
    # print(f"Student {i+1} : {marks[i]}")
# 
# stu_80=np.where(marks>=80)[0]
# print("Students Above 80 :")
# for i in stu_80:
    # print(f"Student {i+1} : {marks[i]}")


# Program 6 – Classroom Data Analyzer

# Given:

# marks = np.array([
    # [78,85,90],
    # [65,72,70],
    # [92,88,95],
    # [45,55,60]
# ])

# Calculate:

# Subject averages.
# Student averages.
# Topper.
# Failed students (average < 50).
# Students scoring above 85 in any subject.

import numpy as np
marks = np.array([
   [78,85,90],
   [65,72,70],
   [92,88,95],
   [45,55,60]
])
subject_avg=np.mean(marks,axis=0)
print("\nSubject Averages:")
for i,avg in enumerate(subject_avg,start=1):
    print(f"Subject {i}: {avg:.2f}")

student_avg=np.mean(marks,axis=1)
print("\nStudent Averages:")
for i,avg in enumerate(student_avg,start=1):
    print(f"Student {i}: {avg:.2f}")

topper=np.max(student_avg)
topper_index=np.argmax(student_avg)
print(f"Topper is Student {topper_index+1} : {topper:.2f}")

fail=np.where(student_avg < 50)[0]
if len(fail)>0:
    for i in fail:
        print(f"Student {i+1} : {student_avg[i]}")
else:
    print("No Students Failed.")

students_above_85=np.where(np.any(marks>=85,axis=1))[0]
print("\nStudents scoring above 85 in any subject")
if len(students_above_85)>0:
    for i in students_above_85:
        print(f"Student {i+1} : {marks[i]}")
else:
    print("\nNo Students Above 85 Marks.")
