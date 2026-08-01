# # Program 1 – Create a Series
# # 
# # Create:
# # 
# # A Series from a list.
# # A Series with custom indexes.
# # Access values using indexes.
# # 
# # Concepts:
# # 
# # pd.Series
# # Indexing
# 
# import pandas as pd
# 
# ages=pd.Series([21,22,22,21])
# print("Ages from a List using Series\n",ages)
# 
# marks=pd.Series([81,85,91,86],index=["Adarsh","James","Govardhan","Manish"])
# print("Marks using Index Names\n",marks)
# print("Accessing Values From Specific Indexes :",marks["Govardhan"])


# # Program 2 – Create Student DataFrame

# # Create a DataFrame containing:

# # Name
# # Age
# # Branch
# # Marks

# # Display:

# # First 3 rows.
# # Last 2 rows.
# # Column names.
# # Shape.
# import pandas as pd
# students={
    # "Name":["Adarsh","James","Manish","Govardhan"],
    # "Age":[22,21,22,21],
    # "Branch":["CSE","AIML","AIML","CSE"],
    # "Marks":[84,82,82,84]
# }

# df=pd.DataFrame(students)
# print("\nFirst 3 Rows:\n",df.head(3))
# print(f"\nLast 2 Rows:\n{df.tail(2)}")
# print(f"\nColumn Names :{df.columns}")
# print(f"Shape is :{df.shape}")

# # Program 3 – Read & Save CSV

# # Create a DataFrame.

# # Save it to:

# # students.csv

# # Read it again using read_csv() and display the contents.

# import pandas as pd
# students={
   # "Name":["Adarsh","James","Manish","Govardhan"],
   # "Age":[22,21,22,21],
   # "Branch":["CSE","AIML","AIML","CSE"],
   # "Marks":[84,82,82,84]
# }
# df=pd.DataFrame(students)
# df.to_csv("students.csv",index=False)

# df=pd.read_csv("students.csv")
# print(df)


# # Program 4 – Dataset Explorer
# 
# # Using your student DataFrame, display:
# 
# # info()
# # describe()
# # dtypes
# # shape
# import pandas as pd
# students={
  # "Name":["Adarsh","James","Manish","Govardhan"],
  # "Age":[22,21,22,21],
  # "Branch":["CSE","AIML","AIML","CSE"],
  # "Marks":[84,82,82,84]
# }
# df=pd.DataFrame(students)
# print(f"\nInformation :")
# df.info()
# print(f"\nStatistical Information :\n{df.describe()}")
# print("\nData Types :\n",df.dtypes)
# print(f"\nShape is :{df.shape}")

# # Program 5 – Data Selection
# # 
# # Practice:
# # 
# # Select one column.
# # Select multiple columns.
# # Use .loc to select a row by label.
# # Use .iloc to select rows by position.

# import pandas as pd
# students={
    # "Name":["Adarsh","James","Manish","Govardhan"],
    # "Age":[22,21,22,21],
    # "Branch":["CSE","AIML","AIML","CSE"],
    # "Marks":[84,82,82,84]
    # }
# df=pd.DataFrame(students)

# print(f"\nFirst Column :\n")
# print(df["Name"])
# print(f"\nMultiple Columns :\n")
# print(df[['Age','Marks']])
# # Using .loc to select a row by label.
# print(f"\nUsing .loc to select a row by label :\n{df.loc[3]}")

# # Use .iloc to select rows by position
# print(f"Using .iloc to select rows by position :\n{df.iloc[3]}")



# Program 6 – Student Report Viewer

# Create a DataFrame with at least 10 students.

# Display:

# Students scoring above 80.
# Average marks.
# Highest marks.
# Lowest marks.

import pandas as pd
students={
    "Name":["Adarsh","James","Manish","Govardhan","Balu","Venkat","Harshith","Raja","Pavan Sai","Sathish"],
    "Roll_No":[31,14,26,34,43,63,61,55,61,50],
    "Branch":["CSE","AIML","AIML","CSE","AI","ML","DS","AIML","ML","CSE"],
    "Marks":[75,82,82,84,86,76,84,82,94,89]
    }
df=pd.DataFrame(students)

# Students scoring above 80.
print(f"Students scoring above 80 :")
print(df.loc[df["Marks"]>80,["Name","Marks"]])
avg=df["Marks"].mean()
print(f"\nAverage of Marks is : {avg:.2f}")
print(f"\nHighesh Marks is :")
print(df.loc[df["Marks"]== df["Marks"].max(),["Name","Marks"]])
print(f"\n Lowest Marks is :")
print(df.loc[df["Marks"]==df["Marks"].min(),["Name","Marks"]])