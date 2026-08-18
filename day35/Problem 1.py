# Program 1 — Complete Classification Pipeline
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
# X/y
 # ↓
# Train/Test Split
 # ↓
# Logistic Regression
 # ↓
# Prediction
 # ↓
# Accuracy
 # ↓
# Precision
 # ↓
# Recall
 # ↓
# F1
 # ↓
# Confusion Matrix
# 
# This should be done without preprocessing first if all your features are numerical.
# 
# The objective is to reinforce the complete ML workflow.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix

df=pd.read_csv("day35/Problem 1.csv")

X=df.drop("Passed",axis=1)

y=df["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model=LogisticRegression()

model.fit(X_train,y_train)

predictions=model.predict(X_test)

print("\nAccuracy is :")
print(accuracy_score(y_test,predictions))

print("\nPrecision is :")
print(precision_score(y_test,predictions))

print("\nRecall is :")
print(recall_score(y_test,predictions))

print("\nF1 Score is :")
print(f1_score(y_test,predictions))

print("\nConfusion matrix is :")
print(confusion_matrix(y_test,predictions))