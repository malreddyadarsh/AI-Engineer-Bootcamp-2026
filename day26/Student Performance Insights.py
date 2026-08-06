# Student Performance Insights
# 
# Build a program that:
# 
# Loads a student CSV file.
# Creates:
# Subject averages.
# Marks distribution.
# Branch distribution.
# Correlation heatmap.
# Study hours vs marks scatter plot.
# Saves all charts to a charts/ folder.
# 
# Skills Used:
# 
# Pandas
# Seaborn
# Matplotlib
# Basic statistics

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("data.csv")

print("Head Of the DataSet :\n",df.head())
print("Basic Information of the DataSet :\n")
df.info()
print("Statistical Information :\n",df.describe())

Subject_Averages=df[["Maths","Science","English"]].mean()
print(f"\nSubject Averages :\n{Subject_Averages}")

# Subject Averages → Bar Plot

sns.barplot(x=Subject_Averages.index,y=Subject_Averages.values)
plt.title("Subject Averages → Bar Plot")
plt.savefig("Day26/Day26_fig1.png")
plt.show()

# Marks Distribution → Histogram

sns.histplot(x="Maths",kde=True,data=df)
plt.title("Marks Distribution → Histogram")
plt.savefig("Day26/Day26_fig2.png")
plt.show()

# Branch Distribution → Count Plot

sns.countplot(x="Branch",data=df)
plt.title("Branch Distribution → Count Plot")
plt.savefig("Day26/Day26_fig3.png")
plt.show()

# Correlation Heatmap

corr=df[["Maths","Science","English","Attendance"]].corr()
print("Correlation Matrix :",corr)
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("Day26/Day26_fig4.png")
plt.show()

# Study Hours vs Marks → Scatter Plot

sns.scatterplot(x="Study_Hours",y="Maths",hue="Branch",data=df,s=100)
plt.title("Study Hours vs Marks → Scatter Plot")
plt.savefig("Day26/Day26_fig5.png")
plt.show()

print(f"\n\nHighest average subject :{Subject_Averages.max():.2f}")

print("\nObservations:")
print("Maths Has a Strong Relationship b/w Science & English.")
print("In HeatMap there are no variables with weak relationships.")