# Program 2 — Student Performance Feature Engineering
# 
# Create:
# 
# Math
# Science
# English
# Study Hours
# Attendance
# Assignments Completed
# Total Assignments
# 
# Create:
# 
# Average Marks
# Assignment Completion Rate
# Study_Attendance
# 
# Then display:
# 
# Original Data
# +
# Engineered Features
# Challenge
# 
# Explain which engineered feature you think will be most useful and why.

import pandas as pd

df=pd.read_csv("day36/Program 2.csv")

df["Average_Marks"]=(df[["Math","Science","English"]].mean(axis=1))

df["Assignment_Completion_Rate"]=df["Assignments_Completed"]/df["Total_Assignments"]

df["Study_Attendance"]=df["Study_Hours"]*df["Attendance"]

df.to_csv("day36/Program2.1.csv",index=False)

df=pd.read_csv("day36/Program2.1.csv")
print(df)