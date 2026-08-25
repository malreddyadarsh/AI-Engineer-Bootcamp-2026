# Program 1 — First Random Forest Classifier
# 
# Create:
# 
# Study Hours
# Attendance
# Previous Marks
# Assignments Completed
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
# RandomForestClassifier
 # ↓
# Train
 # ↓
# Predict
 # ↓
# Accuracy
 # ↓
# Precision
 # ↓
# Recall
 # ↓
# F1


import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score


data = {
    "Study_Hours": [
        2.0, 3.0, 1.5, 5.0, 6.0,
        2.5, 4.0, 7.0, 3.5, 1.0,
        6.5, 5.5, 2.0, 4.5, 7.5,
        3.0, 6.0, 2.5, 5.0, 1.5,
        8.0, 4.0, 6.5, 2.0, 7.0,
        3.5, 5.5, 1.0, 4.5, 8.5
    ],

    "Attendance": [
        65, 70, 55, 80, 90,
        68, 75, 92, 72, 50,
        88, 85, 60, 78, 95,
        69, 91, 64, 82, 58,
        96, 76, 89, 62, 93,
        74, 87, 52, 81, 98
    ],

    "Previous_Marks": [
        55, 62, 48, 72, 85,
        58, 68, 90, 64, 42,
        82, 76, 50, 70, 88,
        60, 91, 56, 75, 45,
        94, 69, 84, 52, 92,
        65, 80, 40, 73, 97
    ],

    "Assignments_Completed": [
        6, 7, 4, 9, 10,
        6, 8, 10, 7, 3,
        9, 9, 5, 8, 10,
        6, 10, 5, 9, 4,
        10, 8, 10, 5, 10,
        7, 9, 3, 8, 10
    ],

    "Passed": [
        0, 1, 0, 1, 1,
        0, 1, 1, 1, 0,
        1, 1, 0, 1, 1,
        0, 1, 0, 1, 0,
        1, 1, 1, 0, 1,
        1, 1, 0, 1, 1
    ]
}

df = pd.DataFrame(data)

X=df[["Study_Hours","Attendance","Previous_Marks","Assignments_Completed"]]

y=df["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("\nOriginal Data :\n",y_test.values)
print("\nPredictions :",y_pred)
print("\nAccuracy :",accuracy_score(y_test,y_pred))
print("\nPrecision Score :",precision_score(y_test,y_pred))
print("\nRecall Score :",recall_score(y_test,y_pred))
print("\nF1 Score :",f1_score(y_test,y_pred))