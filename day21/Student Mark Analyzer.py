# Student Marks Analyzer
# 
# Build a program that:
# 
# Stores marks using NumPy arrays.
# Calculates:
# Student averages.
# Subject averages.
# Highest scorer.
# Lowest scorer.
# Prints a clean summary.
# 
# Skills Used:
# 
# Arrays
# Indexing
# Mathematical functions
# Broadcasting

import numpy as np

marks=np.array([
    [80,86,90,50],
    [45,67,82,40],
    [56,74,45,89],
    [23,78,67,56]
])

student_averages=np.mean(marks,axis=1)
subject_averages=np.mean(marks,axis=0)
total_marks=np.sum(marks,axis=1)
high_scorer=np.argmax(total_marks)
low_scorer=np.argmin(total_marks)


print("=====Student Mark Analyzer=====")
print(f"\nStudent Averages :")
i=1
for avg in student_averages:
    print(f"Student {i} : {avg}")
    i+=1
print(f"\nSubject Averages :")
i=1
for avg in subject_averages:
    print(f"Subject {i} : {avg}")
    i+=1
print(f"Highesh Scorer : Student {high_scorer+1}")
print(f"Loweest Scorer : Student {low_scorer+1}")