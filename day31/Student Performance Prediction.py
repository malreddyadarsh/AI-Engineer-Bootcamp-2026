# Mini Project
# Student Performance Prediction
# 
# Use:
# 
# Features
# Study Hours
# Attendance
# Previous Marks
# Target
# Final Marks
# 
# Your program should:
# 
# Load/create dataset.
# Perform basic EDA.
# Select X and y.
# Split data.
# Train Linear Regression.
# Predict test values.
# Calculate:
# MSE
# RMSE
# R²
# Predict marks for a new student.
# Display actual vs predicted values.
# Create an actual-vs-predicted plot.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# Load/create dataset.
df=pd.read_csv("day31/Student_Performance.csv")

# Perform basic EDA.
print("\nFirst 5 Rows :")
print(df.head())

print("\nDataset Shape :")
print(df.shape)

print("\nColumn Names :")
print(df.columns)

print("\nData Types :")
print(df.dtypes)

print("\nDataset Information :")
df.info()

print("\nDatset Statistical Inforamtion :")
print(df.describe())

print("\nMissing Values in the Dataset :")
print(df.isnull().sum())

print("\nDuplicate Rows :")
print(df.duplicated().sum())

# Select X and y.
X=df[["Study_Hours","Attendance","Previous_Marks"]]

y=df["Final_Marks"]

# Split data.
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Linear Regression.
model=LinearRegression()

model.fit(X_train,y_train)

# Predict test values.
prediction=model.predict(X_test)

# Calculate: MSE  RMSE   R²

mse=mean_squared_error(y_test,prediction)
print("\nMean Squared Error is :",mse)

rmse=mse**0.5
print("\nRoot Mean Squared Error is :",rmse)

r2=r2_score(y_test,prediction)
print("\nR2_Score is :",r2)

# Predict marks for a new student.

new_student=pd.DataFrame({
    "Study_Hours":[6.5],
    "Attendance":[78],
    "Previous_Marks":[70]
})
new_prediction=model.predict(new_student)

print("\nMarks for a New Student is :",new_prediction)

comparsion=pd.DataFrame({
    "Actual_Marks":y_test,
    "Predicted_Marks":prediction
})

print("\nComparsion Of Actual Marks & Predicted Marks :")
print(comparsion)

# Create an actual-vs-predicted plot.
sns.scatterplot(x=y_test,y=prediction)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)
plt.xlabel("Actual_Marks")
plt.ylabel("Predicted_Marks")
plt.title("Comparsion Plot")
plt.show()