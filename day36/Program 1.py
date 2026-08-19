# Program 1 — Create New Features
# 
# Create:
# 
# Age
# Salary
# Experience
# Study Hours
# Attendance
# 
# Create at least these engineered features:
# 
# Salary_per_Experience
# Study_Attendance
# 
# Also create one additional feature of your choice.
# 
# Print:
# 
# Original columns
# New columns
# First 5 rows
# Your goal
# 
# Understand exactly how a raw feature becomes a new feature.


# Salary_per_Experience
# Completion_Rate
# Study_Attendance
# Is_Fresher
# Average_Marks
# Age_Group
# Log_Salary

import pandas as pd
import numpy as np

df=pd.read_csv("day36/Program 1.csv")

df["Salary_per_Experience"]=df["Salary"]/(df["Experience"]+1)

df["Completion_Rate"]=df["Assignments_Completed"]/df["Total_Assignments"]

df["Study_Attendance"]=df["Study_Hours"] * df["Attendance"]

df["Is_Fresher"]=(df["Experience"]==0).astype(int)

df["Average_Marks"]=(df[["Math","Science","English"]].mean(axis=1))

df["Age_Group"]=pd.cut(
    df["Age"],
    bins=[0,25,40,60,100],
    labels=["Young","Adult","Middle_Age","Senior"]
)

df["Log_Salary"]=np.log1p(df["Salary"])

df.to_csv("day36/Problem 1.csv",index=False)

df=pd.read_csv("day36/Problem 1.csv")

print("\nFirst Five Rows of Dataset :")
print(df.head())