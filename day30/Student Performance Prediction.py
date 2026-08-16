# Mini Project
# Student Performance Prediction
# 
# Build a simple ML application that predicts student marks from:
# 
# Study hours
# Attendance
# Previous marks
# Requirements
# Create/load dataset.
# Perform basic EDA.
# Select features.
# Select target.
# Split data.
# Train a regression model.
# Make predictions.
# Display predictions.
# 
# Keep the project simple.
# 
# Don't add a GUI. Don't add unnecessary features.
# 
# The goal is to understand the ML pipeline.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score

data = {
    "Study_Hours": [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    ],

    "Attendance": [
        55, 60, 65, 70, 75, 80, 85, 90, 95, 98,
        62, 68, 72, 78, 83, 87, 91, 94, 96, 99
    ],

    "Previous_Marks": [
        35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
        42, 48, 52, 58, 63, 68, 73, 78, 82, 86
    ],

    "Final_Marks": [
        38, 43, 49, 55, 62, 68, 75, 82, 89, 94,
        45, 51, 57, 64, 70, 76, 81, 87, 91, 96
    ]
}

df=pd.DataFrame(data)

X=df[[
    "Study_Hours",
    "Attendance",
    "Previous_Marks"
]]

y=df["Final_Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=LinearRegression()

model.fit(X_train,y_train)

predictions=model.predict(X_test)

comparisons=pd.DataFrame({
    "Actual":y_test.values,
    "Predicted":predictions
})

print("\nPredictions :")
print(comparisons)

mae=mean_absolute_error(
    y_test,
    predictions
)

r2=r2_score(
    y_test,
    predictions
)

print("\nMODEL EVALUATION")

print("Mean Absolute Error is :",mae)
print("R2 Score is :",r2)