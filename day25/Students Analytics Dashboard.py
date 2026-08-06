# Student Analytics Dashboard
# Features
# Read CSV data.
# Generate:
# Line chart
# Bar chart
# Histogram
# Scatter plot
# Pie chart
# Export charts.
# Summarize statistics.

import pandas as pd
import matplotlib.pyplot as plt

data={
    "Name":["a","b","c","d","e","f","g","h","i","j"],
    "Maths":[45,50,54,58,63,67,70,74,67,80],
    "Social":[85,67,56,67,87,98,45,86,74,64]
     }
df=pd.DataFrame(data)
df.to_csv("Dashboard.csv",index=False)
df["Average"]=df[["Maths","Social"]].mean(axis=1)

# Line chart

plt.plot(df["Name"],df["Maths"],label="Maths",color="red")
plt.plot(df["Name"],df["Social"],label="Social",color="black")
plt.title("Comparsion B/W Maths & Social")
plt.xlabel("Student's Name")
plt.ylabel("Marks")
plt.grid(linestyle="--",alpha=.6)
plt.legend()
plt.savefig("Line_Chart.png")
plt.show()

# Bar chart

plt.bar(df["Name"],df["Average"],label="Average",color="Red",width=0.5)
plt.title("Student's Average")
plt.xlabel("Student's Name")
plt.ylabel("Marks")
plt.grid(axis="y",linestyle="--",alpha=.6)
plt.legend()
plt.savefig("Bar Graph.png")
plt.show()

# Histogram

plt.hist(df["Average"],bins=5,color="blue",label="Average")
plt.title("Marks Distribution")
plt.xlabel("Student's Average")
plt.ylabel("Frequency")
plt.grid(axis="y",linestyle="--",alpha=.6)
plt.legend()
plt.show()

# Scatter plot

plt.scatter(df["Maths"],df["Social"],color="red",s=100,label="Marks")
plt.title("Maths & Social")
plt.xlabel("Maths")
plt.ylabel("Social")
plt.grid(linestyle="--",alpha=.6)
plt.legend()
plt.show()

# Pie chart

df["Result"]=df["Average"].apply(lambda x : "Pass" if x>55 else "Fail")

result=df["Result"].value_counts()

plt.pie(result,labels=result.index,autopct="%1.1f%%",explode=[.1,.1])
plt.title("Final Results")
plt.legend()
plt.show()

print("\n========== DASHBOARD SUMMARY ==========\n")

print("Total Students :", len(df))

print("Highest Average :",
      round(df["Average"].max(),2))

print("Lowest Average :",
      round(df["Average"].min(),2))

print("Overall Average :",
      round(df["Average"].mean(),2))

print("\nTop Student")

print(df.sort_values(
    by="Average",
    ascending=False
).head(1))

print("\nPass / Fail")

print(result)