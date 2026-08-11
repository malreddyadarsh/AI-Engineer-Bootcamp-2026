# # Program 1 – Dataset Overview
# # 
# # Load a CSV file.
# # 
# # Display:
# # 
# # Shape
# # Columns
# # Data types
# # Missing values
# # Duplicate rows
# 
# import pandas as pd
# 
# df=pd.read_csv("day27/sample1.csv")
# # Shape
# print("\nShape of DataSet is :")
# print(df.shape)
# 
# # Columns
# print("\nColumn Names :")
# print(df.columns)
# 
# print("\nData Types of Variables :")
# print(df.dtypes)
# 
# # Missing values
# print("\nMissing Values are :\n")
# print(df.isnull().sum())
# print("\nSum of Missing Values are :",df.isnull().sum().sum())
# 
# # Duplicate rows
# print("\nDuplicated Rows are :")
# print(df.duplicated())
# print("\nSum of Duplicated Rows Are :",df.duplicated().sum())

# # Program 2 – Statistical Summary
# # 
# # Display:
# # 
# # Mean
# # Median
# # Mode
# # Standard deviation
# # Correlation matrix

# import pandas as pd 


# df=pd.read_csv("day27/sample2.csv")

# print(f"\nMean of Marks :")
# print(df["Marks"].mean())

# print(f"\nMedain of Marks :")
# print(df["Marks"].median())

# print(f"\nMode of Marks is :")
# print(df["Marks"].mode())

# print(f"Standard Deviation is :")
# print(df["Marks"].std())

# corr=df[["Study_Hours","Marks","Attendance"]].corr()
# print("Correlation Matrix is :")
# print(corr)


# # Program 3 – Visualization Suite

# # Generate:

# # Histogram
# # Box Plot
# # Count Plot
# # Scatter Plot
# # Heatmap


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_theme(style="whitegrid")
# df=pd.read_csv("day27/sample3.csv")
# print("\nObservations:")

# # Histogram
# sns.histplot(x="Marks",kde=True,data=df,label="Marks")
# plt.title("Marks Distribution")
# plt.legend()
# plt.show()
# print("\n1.Most of the Students Scored Marks Between 80 and 90.")

# # Box Plot
# sns.boxplot(x="Gender",y="Attendance",data=df)
# plt.title("Gender Vs Attendence")
# plt.show()
# print("\n2.Outliers are found in the Attendance that is one of the male students is havind Attendance of : 40 which differs from others.")

# # Count Plot
# sns.countplot(x="Branch",data=df,label="Branches")
# plt.title("Categories Analysis ")
# plt.show()
# print("\n3. Most Common Category is : CSE\nLeast Common Category is : ECE & IT")

# # Scatter Plot
# sns.scatterplot(x="Study_Hours",y="Marks",hue="Branch",s=100,data=df)
# plt.title("RelationShip Analysis")
# plt.show()
# print("\n4.Positive RelationShip b/w Study_Hours & Marks")

# # Heatmap

# corr=df[["Age","Study_Hours","Marks","Attendance"]].corr()
# print("Correlational Matrix is :\n",corr)
# sns.heatmap(corr,annot=True,cmap="coolwarm")
# plt.title("Relationships ")
# plt.show()
# print("\n5.Strongest Positive Relationship is : Marks VS Study_Hours\nWeakest Postive Realationship is : Age VS Attendence")


# # Program 4 – Student Performance Analysis
# 
# # Find:
# 
# # Top performer
# # Lowest performer
# # Subject averages
# # Pass percentage
# 
# # Write three insights from your analysis.
# 
# import pandas as pd
# 
# 
# df=pd.read_csv("day27/sample4.csv")
# 
# df["Average"]=df[["Maths","Science","Python"]].mean(axis=1)
# 
# print("=====Top Performer =====")
# topper=df["Average"].max()
# student=df.loc[df["Average"]==topper]
# print(student[["Name","Average"]])
# 
# print("\n=====Lowest Performer =====")
# lowest=df["Average"].min()
# student=df.loc[df["Average"]==lowest]
# print(student[["Name","Average"]])
# 
# # Subject Averages
# subject_averages=df[["Maths","Science","Python"]].mean()
# print("\n=====Subject Averages=====")
# print(subject_averages)
# 
# #Pass Percentage
# 
# passed_students=df[(df["Maths"]>50) & (df["Science"]>50) & (df["Python"]>50)]
# pass_percentage=(len(passed_students)/len(df))*100
# print("\nPassed Percentage is :",pass_percentage)
# 
# #Three Insights from Analysis
# print("\nThree Insights from Analysis")
# print("1.Python has the highest Average.")
# print("2.The Student having high attendence can score high marks.")
# print("3.The Pass Percentage tells that the almost every student who scored  above 50 in Each Subject had been passed.")


