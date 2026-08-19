# Program 3 — Binning + Log Transformation
# 
# Create a dataset:
# 
# Age
# Salary
# 
# Perform:
# 
# Age binning
# 
# Create:
# 
# Young
# Adult
# Middle_Age
# Senior
# 
# using:
# 
# pd.cut()
# Salary transformation
# 
# Create:
# 
# Log_Salary
# 
# using:
# 
# np.log1p()
# 
# Then compare:
# 
# Salary
# Log_Salary
# 
# using a histogram.
# 
# Your goal is to visually understand why transformations can be useful.

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv("day36/Problem 3.csv")

df["Age_Group"]=pd.cut(
    df["Age"],
    bins=[0,25,40,60,100],
    labels=[
        "Young","Adult","Middle_Age","Senior"
    ]
)

df["Log_Salary"]=np.log1p(df["Salary"])

# Compare Salary and Log_Salary
plt.figure(figsize=(10, 5))

sns.histplot(
    df["Salary"],
    kde=True,
    bins=10
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()


plt.figure(figsize=(10, 5))

sns.histplot(
    df["Log_Salary"],
    kde=True,
    bins=10
)

plt.title("Log Salary Distribution")
plt.xlabel("Log_Salary")
plt.ylabel("Frequency")

plt.show()