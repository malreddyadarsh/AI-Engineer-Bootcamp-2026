# # Program 1 – Missing Value Analyzer
# # 
# # Create a DataFrame with some missing values.
# # 
# # Display:
# # 
# # Missing values in each column.
# # Total missing values.
# # 
# # Concepts:
# # 
# # isnull()
# # sum()
# 
# import pandas as pd
# 
# data={
    # "Name":["Adarsh",None,"James"],
    # "Age":[22,None,24],
    # "Marks":[None,87,None]
# }
# df=pd.DataFrame(data)
# 
# print("Original DataFrame:\n")
# print(df)
# 
# print("\nMissing Values are named as True :\n",df.isnull())
# 
# print("\nMissing Values in Each Column:")
# print(df.isnull().sum())
# 
# print("\nTotal missing values :",df.isnull().sum().sum())


# # Program 2 – Fill Missing Data

# # Replace:

# # Missing marks with average marks.
# # Missing names with "Unknown".

# # Concepts:

# # fillna()

# import pandas as pd 

# data={
  # "Name":["Adarsh",None,"James"],
  # "Age":[22,None,24],
  # "Marks":[None,87,None]
# }

# df=pd.DataFrame(data)

# print("\nPrinting the Data Set Before Filling Missing Values :\n",df)

# # Missing marks with average marks.
# df["Marks"]=df["Marks"].fillna(df["Marks"].mean())

# # Missing names with "Unknown".
# df["Name"]=df["Name"].fillna("Unknown")

# # Additional
# # Missing Age with average age
# df["Age"]=df["Age"].fillna(df["Age"].mean())

# print("\nPrinting the Data Set After Filling Missing Values :\n",df)


# Program 3 – Duplicate Remover

# Create duplicate student records.

# Display:

# Duplicate rows.
# Dataset after removing duplicates.

# Concepts:

# duplicated()
# drop_duplicates()

import pandas as pd
data={
    "Name":["Adarsh","James",None,"James"],
    "Age":[22,22,None,22],
    "Marks":[91,None,90,None]
}

df=pd.DataFrame(data)

print("Duplicate Student Records :\n",df)

# Duplicate rows.
print("\nDuplicate rows are :\n",df.duplicated())
print("\nTotal Duplicate Rows are :",df.duplicated().sum()) # Additional

# Dataset after removing duplicates.
df=df.drop_duplicates()
print("\n# Dataset after removing duplicates is :\n",df)


# # Program 4 – Student Filter
# 
# # Display:
# 
# # Students scoring above 80.
# # Students between ages 20 and 25.
# # Students from the AIML branch.
# 
# import pandas as pd
# 
# data={
    # "Name":["Adarsh","James","Manish","Venkat"],
    # "Age":[21,22,24,19],
    # "Branch":["CSE","AIML","AIML","CSE"],
    # "Marks":[81,75,86,76]
# }
# 
# df=pd.DataFrame(data)
# 
# # Students scoring above 80.
# print("\nStudents scoring above 80 :\n")
# print(df[df["Marks"]>80])
# 
# # Students between ages 20 and 25
# print("\nStudents between ages 20 and 25 : \n")
# print(df[(df["Age"]>20) & (df["Age"]<25)])
# 
# # Students from the AIML branch
# print("\nStudents from the AIML branch:\n")
# print(df[df["Branch"] == "AIML"])


# # Program 5 – Sorting & Renaming
# # 
# # Practice:
# # 
# # Rename columns.
# # Sort by marks.
# # Sort by age.

# import pandas as pd

# data={
    # "Nm":["Adarsh","James","Manish","Venkat"],
    # "ag":[21,23,24,25],
    # "mak":[90,86,45,92]
# }

# df=pd.DataFrame(data)

# print("\n Printing Dataset Before Doing any Operations :\n",df)

# # Rename columns.

# df=df.rename(columns={
    # "Nm":"Name",
    # "ag":"Age",
    # "mak":"Mark"
# })

# print("\nPrinting Dataset After Renaming Columns :\n",df)

# # Sort by marks.
# print("\nSorting  by marks In Descending Order :\n")
# print(df.sort_values("Mark",ascending=False))

# # Sort by age.
# print("\nSorting  by Age In Ascending Order :\n")
# print(df.sort_values("Age"))


## Program 6 – Student Grade Processor
## 
## Create a new column called Grade.
## 
## Rules:
## 
## 90+ → A
## 80–89 → B
## 70–79 → C
## Below 70 → D
## 
## Use apply() to generate grades.

#import pandas as pd

#data={
    #"Name":["Adarsh","James","Manish","Venkat"],
    #"Age":[21,23,24,25],
    #"Marks":[90,86,45,92]
#}


#df=pd.DataFrame(data)

#print("\nPrinting Dataset Before Adding Grade Column :\n",df)
#def grade(mark):
    #if mark>=90:
        #return "A"
    #elif mark>=80:
        #return "B"
    #elif mark>=70:
        #return "C"
    #else :
        #return "D"

#df["Grade"]=df["Marks"].apply(grade)

#print("\nPrinting Dataset After Adding Grade Column :\n",df)