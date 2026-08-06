# # Program 1 – Student Performance Analysis
# # 
# # Dataset:
# # 
# # Student
# # Marks
# # 
# # Create:
# # 
# # Line Plot
# # Bar Plot
# 
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
# students={
    # "Name":["A","B","C","D","E","F","G","H","I","J"],
    # "Marks":[76,89,95,56,73,58,98,76,90,58],
    # "Gender":["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"]
# }
# 
# df=pd.DataFrame(students)
# 
# # Line Plot
# sns.set_theme(style="whitegrid")
# sns.lineplot(x="Name",y="Marks",data=df,label="Marks")
# plt.title("Name By Marks")
# plt.legend()
# plt.show()
# 
# # Bar Plot
# 
# sns.barplot(x="Gender",y="Marks",data=df,label="Marks")
# plt.title("Bar Graph of Gender By Marks")
# plt.legend()
# plt.show()

# # Program 2 – Branch Distribution

# # Dataset:

# # AIML
# # CSE
# # ECE
# # EEE

# # Create:

# # Count Plot
# # Pie Chart (using Matplotlib for comparison)

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# employees ={
    # "Department":["AIML","EEE","CSE","ECE","EEE","CSE","AIML","ECE","AIML","EEE"]
# }
# df=pd.DataFrame(employees)
# #count plot

# sns.countplot(x="Department",data=df)
# plt.title("Count Plot")
# plt.show()

# # Pie Chart (using Matplotlib for comparison)

# counts=df["Department"].value_counts()

# plt.pie(counts,labels=counts.index,autopct="%1.1f%%",explode=[0.1,.1,.1,.1])
# plt.title("Branch Distribution")
# plt.show()

# # Program 3 – Marks Distribution
# # 
# # Create:
# # 
# # Histogram
# # Box Plot
# # 
# # Identify:
# # 
# # Average range
# # Outliers
# # Overall distribution

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# students={
    # "Name":["a","b","c","d","e","f","g","h","i","j"],
    # "Math":[45,67,78,56,90,88,60,72,81,69],
    # "Science":[50,65,80,60,92,90,58,75,84,70],
    # "Hours":[2,3,4,3,7,6,2,5,6,4],
    # "Gender":["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"]
# }

# df=pd.DataFrame(students)

# # Histogram
# sns.histplot(x="Math",bins=5,kde=True,data=df)
# plt.title("Histogram")
# plt.show()

# # Box Plot
# sns.boxplot(x="Gender",y="Science",data=df)
# plt.title("Box Plot")
# plt.show()

# print("Average Math Marks :", df["Math"].mean())
# print("Average Science Marks :", df["Science"].mean())

# print("\nObservation:")
# print("1. Most Math marks are between 60 and 90.")
# print("2. No significant outliers are present.")
# print("3. Distribution is approximately balanced.")


# # Program 4 – Study Hours vs Marks

# # Create a scatter plot.

# # Ask:

# # Is there a positive relationship?

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# students={
    # "Name":["a","b","c","d","e","f","g","h","i","j"],
    # "Math":[45,67,78,56,90,88,60,72,81,69],
    # "Science":[50,65,80,60,92,90,58,75,84,70],
    # "Hours":[2,3,4,3,7,6,2,5,6,4],
    # "Gender":["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"]
# }


# df=pd.DataFrame(students)

# sns.scatterplot(x="Hours",y="Math",data=df)
# plt.title("Study Hours vs Marks")
# plt.show()

# print("\nObservations :")
# print("Based on the Scattered points in the graph , there is an positive relationship b/w Hours & Maths")


# # Program 5 – Correlation Heatmap

# # Create a dataset with:

# # Maths
# # Science
# # English
# # Attendance

# # Generate:

# # Correlation matrix
# # Heatmap

# # Interpret:

# # Which variables move together?
# # Which relationships appear weak?

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# students={
    # "Name":["A","B","C","D","E","F"],
    # "Maths":[40,50,60,70,80,90],
    # "Science":[89,56,34,55,45,76],
    # "English":[76,54,46,86,96,75],
    # "Attendance":[56,89,45,67,69,75]
# }

# df=pd.DataFrame(students)

# corr=df[["Maths","Science","English","Attendance"]].corr()
# print(corr)

# sns.heatmap(corr,annot=True,cmap="coolwarm")
# plt.title("HeatMap")
# plt.show()

# print("\nObservations:")
# print("1. Maths and English show the strongest positive relationship (0.45).")
# print("2. Maths and Science have a weak negative relationship (-0.20).")
# print("3. English and Attendance have a very weak positive relationship (0.14).")
# print("4. Overall, no variables show a strong correlation.")


# Program 6 – Complete Visualization Dashboard

# Create one program that generates:

# Line Plot
# Bar Plot
# Count Plot
# Histogram
# Box Plot
# Scatter Plot
# Heatmap

# Save every figure.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

students = {
    "Name": [
        "Adarsh", "James", "Manish", "Raja", "Pavan",
        "Harshith", "Venkat", "Balu", "Rohit", "Kiran",
        "Sai", "Anil"
    ],

    "Maths": [
        45, 56, 67, 72, 81,
        90, 76, 64, 58, 85,
        69, 94
    ],

    "Science": [
        50, 60, 65, 74, 84,
        92, 78, 68, 55, 88,
        72, 95
    ],

    "English": [
        55, 62, 70, 75, 83,
        91, 80, 66, 60, 87,
        74, 93
    ],

    "Hours": [
        2, 3, 4, 5, 6,
        7, 5, 4, 3, 6,
        5, 8
    ],

    "Attendance": [
        82, 85, 88, 90, 93,
        96, 91, 87, 84, 95,
        89, 98
    ],

    "Gender": [
        "Male", "Male", "Male", "Male", "Male",
        "Male", "Male", "Male", "Male", "Male",
        "Female", "Female"
    ],

    "Department": [
        "AIML", "CSE", "ECE", "AIML", "EEE",
        "CSE", "ECE", "AIML", "EEE", "CSE",
        "AIML", "ECE"
    ]
}

df=pd.DataFrame(students)
# Line Plot (Hours vs Maths)

sns.lineplot(x="Hours",y="Maths",data=df,marker="o",color="red")
plt.title("Hours vs Maths")
plt.show()

# Bar Plot (Department vs average Maths or Science)

sns.barplot(x="Department",y="Maths",data=df)
plt.title("Department vs average Maths")
plt.show()

# Count Plot (Department or Gender)

sns.countplot(x="Gender",data=df)
plt.title("Count Plot of Gender")
plt.show()

# Histogram (Maths, Science, English, etc.)

sns.histplot(x="English",kde=True,data=df)
plt.title("Histogram English")
plt.show()

# Box Plot (Gender vs Maths/Science)

sns.boxplot(x="Gender",y="Maths",data=df)
plt.title("Gender vs Maths")
plt.show()

# Scatter Plot (Hours vs Maths or Science)

sns.scatterplot(x="Hours",y="Science",hue="Department",data=df)
plt.title("Hours vs Science By Department")
plt.show()

# Heatmap (Correlation among Maths, Science, English, Hours, Attendance)

corr=df[["Maths","Science","English","Hours","Attendance"]].corr()
print(corr)

sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()