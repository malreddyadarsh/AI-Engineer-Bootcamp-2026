# 3. Mini Project
# Student Admission Prediction Pipeline
# 
# Create a dataset containing:
# 
# Age
# Study Hours
# Attendance
# Previous Marks
# City
# Branch
# Admission
# 
# Target:
# 
# Admission
# 
# Build:
# 
# Load Dataset
      # ↓
# EDA
      # ↓
# X / y
      # ↓
# Train/Test Split
      # ↓
# Identify numerical columns
      # ↓
# Identify categorical columns
      # ↓
# StandardScaler
      # ↓
# OneHotEncoder
      # ↓
# ColumnTransformer
      # ↓
# Logistic Regression
      # ↓
# Pipeline
      # ↓
# Predictions
      # ↓
# Accuracy
      # ↓
# Precision
      # ↓
# Recall
      # ↓
# F1


import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score)

df=pd.read_csv("day34/program1.csv")

# EDA

print("\nFirst Five Rows of Dataset :")
print(df.head())

print("\nMissin Values in The Dataset :")
print(df.isnull().sum())

print("\nBasic Information of the Dataset :")
df.info()

print("\nStatistical Information of the Dataset :")
print(df.describe())

# X / y
X=df[["Age","Study_Hours","Attendance","City","Branch","Previous_Marks"]]

y=df["Admission"]

# Train/Test Split
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Identify numerical columns
numerical_columns=["Age","Study_Hours","Attendance","Previous_Marks"]
# Identify categorical columns
categorical_columns=["City","Branch"]

preprocessor=ColumnTransformer(
    transformers=[
        ("num",StandardScaler(),numerical_columns),
        ("cat",OneHotEncoder(),categorical_columns)
    ]
)

pipeline=Pipeline([
    ("preprocessor",preprocessor),
    ("model",LogisticRegression())
])

pipeline.fit(X_train,y_train)

predictions=pipeline.predict(X_test)

print("\nAccuracy Score :")
print(accuracy_score(y_test,predictions))

print("\nPrecision Score :")
print(precision_score(y_test,predictions))

print("\nRecall Score :")
print(recall_score(y_test,predictions))

print("\nF1 Score :")
print(f1_score(y_test,predictions))