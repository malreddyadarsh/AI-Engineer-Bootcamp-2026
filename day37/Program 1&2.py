# Program 1 — Your First Decision Tree Classifier
# 
# Create:
# 
# Study Hours
# Attendance
# Previous Marks
# Passed
# 
# Build:
# 
# Dataset
 # ↓
# X / y
 # ↓
# Train/Test Split
 # ↓
# DecisionTreeClassifier
 # ↓
# Train
 # ↓
# Predict
 # ↓
# Accuracy
# 
# Start with:
# 
# DecisionTreeClassifier(
    # random_state=42
# )
# 
# Don't set max_depth initially.
# 
# See what happens.

import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.DataFrame({
    "Study_Hours": [
        1, 2, 2, 3, 3,
        4, 4, 5, 5, 6,
        6, 7, 7, 8, 8,
        9, 9, 10, 10, 11
    ],

    "Attendance": [
        55, 60, 62, 65, 68,
        70, 72, 74, 76, 78,
        80, 82, 84, 85, 87,
        88, 90, 92, 94, 96
    ],

    "Previous_Marks": [
        40, 42, 45, 48, 50,
        52, 55, 58, 60, 63,
        65, 68, 70, 73, 75,
        78, 80, 84, 87, 90
    ],

    "Passed": [
        0, 0, 0, 0, 0,
        0, 0, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
})


X=data[["Study_Hours","Attendance","Previous_Marks"]]

y=data["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

depths=[1,2,3,5,10]
for depth in depths:
    model=DecisionTreeClassifier(
    max_depth=depth,
    random_state=42
)
    model.fit(X_train,y_train)
    predictions= model.predict(X_test)
    accuracy=accuracy_score(y_test,predictions)
    print("\nDepth :",depth)
    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)
    print("Training Accuracy :", train_accuracy)
    print("Testing Accuracy  :", test_accuracy)
    print("-----------------------------")