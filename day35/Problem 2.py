# Program 2 — Pipeline with Preprocessing
# 
# Create:
# 
# Age
# Salary
# Experience
# City
# Education
# Passed
# 
# Use:
# 
# Numerical → StandardScaler
# Categorical → OneHotEncoder
# 
# Then:
# 
# ColumnTransformer
        # ↓
# Pipeline
        # ↓
# LogisticRegression
        # ↓
# Evaluation
# 
# This program connects Day 34 + Day 35.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("day35/Problem 2.csv")

X=df.drop("Passed",axis=1)

y=df["Passed"]

numerical_columns=["Age","Salary","Experience"]

categorical_columns=["City","Education"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

preprocessor=ColumnTransformer(
    transformers=[
        ("num",StandardScaler(),numerical_columns),
        ("cat",OneHotEncoder(),categorical_columns)
    ]
)

Model=Pipeline([
    ("preprocessor",preprocessor),
    ("model",LogisticRegression())
])

Model.fit(X_train,y_train)

predictions=Model.predict(X_test)

print("\nActual Values :")
print(y_test.values)

print("\nPredicted Values :")
print(predictions)