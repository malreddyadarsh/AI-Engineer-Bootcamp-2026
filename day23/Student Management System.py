# Student Information Manager
# 
# Build a program that:
# 
# Stores student information in a Pandas DataFrame.
# Saves the data to a CSV file.
# Loads the CSV file.
# Displays:
# Number of students.
# Average marks.
# Highest scorer.
# Lowest scorer.
# Allows viewing selected columns.
# 
# Concepts Used:
# 
# DataFrame
# CSV
# Selection
# Statistics

import pandas as pd
students={
    "Name":["Adarsh","James","Manish","Govardhan","Balu","Venkat","Harshith","Raja","Pavan Sai","Sathish"],
    "Roll_No":[31,14,26,34,43,63,61,55,61,50],
    "Branch":["CSE","AIML","AIML","CSE","AI","ML","DS","AIML","ML","CSE"],
    "Marks":[75,82,82,84,86,76,84,82,94,89]
    }
df=pd.DataFrame(students)
# Saves the data to a CSV file
df.to_csv("Students.csv",index=False)
# Loads the CSV file
dg=pd.read_csv("Students.csv")
students_len=dg.shape[0]
print("\nNumber of Students are :",students_len)

avg=dg["Marks"].mean()
print(f"\nAverage Marks is :{avg:.2f}")

print("\nHighest Scorer is :")
print(dg.loc[dg["Marks"]== dg["Marks"].max(),["Name","Marks"]])

print("\nLowest Scorer is :")
print(dg.loc[dg["Marks"]== dg["Marks"].min(),["Name","Marks"]])

# Allows viewing selected columns
print("\nSelected Columns (Name and Roll_No):")
print(dg[["Name","Roll_No"]])