# Student Performance Visualizer
# 
# Features:
# 
# Load student marks from a CSV.
# Display:
# Subject-wise average.
# Top 4 students.
# Marks distribution.
# Pass vs Fail.
# Save charts as PNG files.
# 
# Skills Used:
# 
# Pandas
# Matplotlib
# CSV
# Basic analysis

import pandas as pd
import matplotlib.pyplot as plt

data={
    "Name":["Adarsh","James","Venkat","Manish","Balu","Govardhan",],
    "Maths":[86,78,34,56,78,76],
    "Physics":[45,67,24,46,67,87],
    "Chemistry":[58,56,34,57,57,58]
}

df=pd.DataFrame(data)
df.to_csv("basic_students.csv",index=False)

df=pd.read_csv("basic_students.csv")


df["Average"]=df[["Maths","Physics","Chemistry"]].mean(axis=1)


# Subject-wise average.

subject_avg=df[["Maths","Physics","Chemistry"]].mean()


plt.bar(subject_avg.index,subject_avg.values,width=.5,label="Average",color=["red","green","blue"])
plt.title("Subject-wise average")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.legend()
plt.savefig("Subject_wise_average.png")
plt.show()

# Top 4 students.

top_students = df.sort_values(by="Average",ascending=False).head(4)

plt.bar(top_students["Name"],top_students["Average"],color="orange",label="Average")
plt.title("Top 4 Students ")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.legend()
plt.savefig("top_4.png")
plt.show()

#  Marks distribution

plt.hist(df["Average"],bins=3,color="red",label="Average")
plt.title("Marks Distribution")
plt.xlabel("Average Marks")
plt.ylabel("Frequency")

plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.savefig("marks_distribution.png")

plt.show()


# Pass / Fail
# -----------------------------

df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

result = df["Result"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    result,
    labels=result.index,
    autopct="%1.1f%%",
    explode=[0.05,0.05]
)

plt.title("Pass vs Fail")

plt.savefig("pass_fail.png")

plt.show()
