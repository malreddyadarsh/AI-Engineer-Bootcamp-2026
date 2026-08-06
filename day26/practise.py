# Features
# Load student data into a Pandas DataFrame.
# Display dataset summary (head(), info(), describe()).
# Generate:
# Line Plot (Study Hours vs Math Marks)
# Bar Plot (Average Science Marks by Gender)
# Count Plot (Students by Gender)
# Histogram (Math Marks Distribution)
# Box Plot (Math Marks by Gender)
# Scatter Plot (Study Hours vs Science Marks with Gender as Hue)
# Heatmap (Correlation Matrix)
# Add titles to all plots.
# Use sns.set_theme(style="whitegrid") for consistent styling.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

students={
    "Name":["a","b","c","d","e","f","g","h","i","j"],
    "Math":[45,67,78,56,90,88,60,72,81,69],
    "Science":[50,65,80,60,92,90,58,75,84,70],
    "Hours":[2,3,4,3,7,6,2,5,6,4],
    "Gender":["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"]
}

df=pd.DataFrame(students)

print("\nHead of The DataFrame is :\n",df.head())
print("\nPrinting INFO of the DataFrame is :\n")
df.info()
print("\nPrinting Statistical Information :\n")
print(df.describe())


# Line Plot (Study Hours vs Math Marks)
sns.set_theme(style="whitegrid")
sns.lineplot(x="Hours",y="Math",data=df,label="Marks")
plt.title("Study Hours vs Math Marks")
plt.legend()
plt.show()

# Bar Plot (Average Science Marks by Gender)

sns.set_theme(style="whitegrid")
sns.barplot(x="Gender",y="Science",data=df,label="Marks")
plt.title("Average Science Marks by Gender")
plt.legend()
plt.show()

# Count Plot (Students by Gender)

sns.countplot(x="Gender",data=df)
plt.title("Students by Gender")
plt.show()

# Histogram (Math Marks Distribution)

sns.histplot(x="Math",bins=5,kde=True,data=df)
plt.title("Math Marks Distribution")
plt.show()

# Box Plot (Math Marks by Gender)

sns.boxplot(x="Gender",y="Math",data=df)
plt.title("Math Marks by Gender")
plt.show()


# Scatter Plot (Study Hours vs Science Marks with Gender as Hue)

sns.scatterplot(x="Hours",y="Science",hue="Gender",data=df)
plt.title("Study Hours vs Science Marks with Gender as Hue")
plt.show()

# Heatmap (Correlation Matrix)

corr=df[["Math","Science","Hours"]].corr()

print(corr)

sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()