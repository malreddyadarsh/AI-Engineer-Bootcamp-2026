# Exploratory Data Analysis Dashboard
# Features
# Load any CSV.
# Display summary statistics.
# Missing value report.
# Duplicate report.
# Interactive menu (console-based).
# Generate:
# Histogram
# Scatter Plot
# Box Plot
# Count Plot
# Heatmap
# Export charts.
# Save analysis report.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

df=pd.read_csv("day27/data.csv")

# Missing value report & Filling Them 

print("\n====Missing Values in Each Columns====\n",df.isnull().sum())
print("\nTotal Missing Values are :",df.isnull().sum().sum())

df["Study_Hours"]=df["Study_Hours"].fillna(method="ffill")
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
df["Attendance"]=df["Attendance"].fillna(method="bfill")

# Duplicate report & Removing them 
print("\nNo.of Duplicated Rows are :",df.duplicated().sum())
df.drop_duplicates(inplace=True)

# Display summary statistics.
print("\n=====Information of the Dataset=====\n")
df.info()
print("\n=====Statistical Information of the Dataset=====\n")
print(df.describe())

def Menu():
    print("\n===Exploratory Data Analysis Dashboard===\n")
    print("1. Histogram")
    print("2. Scatter Plot")
    print("3. Box Plot")
    print("4. Count Plot")
    print("5. Heatmap")
    print("6. Exit")

while True:
    Menu()
    ch=int(input("\nEnter Your Choice :"))
    if ch==1:
        #1. Histogram
        sns.histplot(x="Marks",kde=True,bins=10,data=df,label="Marks")
        plt.title("Marks Distribution")
        plt.legend()
        plt.savefig("day27/Histogram=Marks Distribution")
        plt.show()
    elif ch==2:
        #2. Scatter Plot
        sns.scatterplot(x="Marks",y="Study_Hours",hue="Branch",data=df,s=100)
        plt.title("Relationship Analysis")
        plt.savefig("day27/ScatterPlot=Relationship Analysis")
        plt.show()
    elif ch==3:
        #3. Box Plot
        sns.boxplot(x="Gender",y="Marks",data=df)
        plt.title("Outliers")
        plt.savefig("day27/BoxPlot=ToFindOutliers")
        plt.show()
    elif ch==4:
        #4. Count Plot
        sns.countplot(x="Gender",data=df,label="Gender")
        plt.title("Categorical Analysis")
        plt.legend()
        plt.savefig("day27/CountPlot=Categorical Analysis")
        plt.show()
    elif ch==5:
        #5. Heatmap
        corr=df[["Study_Hours","Marks","Attendance"]].corr()
        sns.heatmap(corr,annot=True,cmap="coolwarm")
        plt.title("Correlation Matrix")
        plt.savefig("day27/HeatMap=Correlation Matrix")
        plt.show()
    elif ch==6:
        print("Thank You For Choosing !")
        break
    else:
        print("Invalid Option.")

