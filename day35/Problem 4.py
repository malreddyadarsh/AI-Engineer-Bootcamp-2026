# Program 4 — Prediction for a New Student
# 
# After training your pipeline, create a completely new student:
# 
# Age = 24
# Salary = 45000
# Experience = 2
# City = Hyderabad
# Education = B.Tech
# 
# Use:
# 
# model.predict(new_student)
# 
# and:
# 
# model.predict_proba(new_student)
# 
# The new student's data must go through the same preprocessing pipeline.
# 
# You should not manually encode or scale it.
# 
# That's one of the biggest advantages of using a Pipeline.

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

df=pd.read_csv("day35/Problem 4.csv")

X=df.drop("Passed",axis=1)

y=df["Passed"]

numerical_columns=["Age","Salary","Experience"]

categorical_columns=["City","Education"]

new_student=pd.DataFrame ({
    "Age" :[24],
    "Salary":[45000],
    "Experience":[2],
    "City":["Hyderabad"],
    "Education":["B.Tech"]
})
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
        ("cat",OneHotEncoder(handle_unknown="ignore"),categorical_columns)
    ]
)

model=Pipeline([
    ("preprocessor",preprocessor),
    ("model",LogisticRegression())
])

model.fit(X_train,y_train)

predictions=model.predict(new_student)

print("\nPrediction of New Student is :")
print(predictions)

probability = model.predict_proba(new_student)

print("\nPrediction Probability:")
print(probability)