# Student Data Dashboard
# Features
# Load student records from CSV.
# Display dataset summary.
# Search students by name.
# Filter students by marks.
# Save updated records.

import pandas as pd
students={
    "Name":["Adarsh","James","Manish","Govardhan","Balu","Venkat","Harshith","Raja","Pavan Sai","Sathish"],
    "Roll_No":[31,14,26,34,43,63,61,55,61,50],
    "Branch":["CSE","AIML","AIML","CSE","AI","ML","DS","AIML","ML","CSE"],
    "Marks":[75,82,82,84,86,76,84,82,94,89]
    }
df=pd.DataFrame(students)
df.to_csv("StudentData.csv",index=False)
df=pd.read_csv("StudentData.csv")
while True:
    print("----------------------------------------")
    print("=====Student Data DashBoard=====")
    print("1. Display Dataset Summary")
    print("2. Search Student by Name")
    print("3. Filter Students by Marks")
    print("4. Save Updated Records")
    print("5. Exit")
    ch=int(input("Enter your Choice:"))
    if ch==1:
        print("\nNo.of Students are :",df.shape[0])
        print("\nNo.of Columns are :",df.shape[1])
        print("\nData Types :\n",df.dtypes)
        print("\nColumn names :",df.columns)
        print("\nStudent Data Information :")
        df.info()
        print("\nStatistical Summary is :\n")
        print(df.describe())
    elif ch==2:
        name=input("Enter Student to Search In the CSV File :")
        student=df.loc[df["Name"] == name]
        if not student.empty:
            print("Student Found Succesffully in the CSV File.")
        else:
            print("No Student Name Found.")
    elif ch==3:
        marks=int(input("Enter Student Marks For Filtering :"))
        filtered = df.loc[df["Marks"] >= marks, ["Name", "Marks"]]
        if not filtered.empty:
            print(filtered)
        else:
            print("No students found with marks greater than or equal to", marks)   
    elif ch==4:
        df.to_csv("StudentData.csv",index=False)
        print("Saved Updatesd Records Successfully.")
    elif ch==5:
        print("Thank You For Choosing.")
        break
    else:
        print("Invalid Input.")