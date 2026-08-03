# Student Data Cleaning Tool
# 
# Build a console application that:
# 
# Loads student data from a CSV file.
# Detects missing values.
# Fills missing values.
# Removes duplicate rows.
# Renames columns.
# Sorts by marks.
# Saves the cleaned dataset as a new CSV file.

import pandas as pd

data={
    "nm":["Adarsh",None,"James","Manish","Raja","Adarsh"],
    "ag":[21,23,None,22,None,21],
    "mk":[86,75,None,None,89,86]
}

df=pd.DataFrame(data)
df.to_csv("Data_Student.csv",index=False)

df=pd.read_csv("Data_Student.csv")

print("\nPrinting Read CSV File:\n",df)
print("\nDetects missing values :\n")
if df.isnull().sum().sum()>0:
    print(df.isnull().sum())
else :
    print("\nNo Missing Values.")

print("\nTotal Number of Missing Values are :",df.isnull().sum().sum())

# Fills missing values
df["nm"]=df["nm"].fillna("Unknown")

df["ag"]=df["ag"].fillna(method="ffill")

df["mk"]=df["mk"].fillna(df["mk"].mean())

print("\nPrinting Dataset After Filling Missing Values :\n")
print(df)

# Removes duplicate rows.
print("\nDuplicates Rows are :\n",df.duplicated())
print("\nNumber of Duplicate Rows is :",df.duplicated().sum())
df=df.drop_duplicates()
print("\nPrinting Dataset After Removing Duplicates Rows :\n")
print(df)

# Renames columns.
df=df.rename(columns={
    "nm":"Name",
    "ag":"Age",
    "mk":"Marks"
})

print("\nPrinting Dataset After Renaming Columns :\n")
print(df)

# Sorts by marks.
print("\nPrinting Dataset of Sorted Marks in Ascending Order.\n")
print(df.sort_values("Marks"))

print("\nPrinting Dataset Before Saving it to a New CSV File :\n")
print(df)

# Saves the cleaned dataset as a new CSV file.
df.to_csv("New_Student_Data.csv",index=False)
print("\nStudent Dataset is added into a New CSV File.")