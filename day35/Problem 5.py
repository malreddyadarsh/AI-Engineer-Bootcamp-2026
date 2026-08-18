# Program 5 — Save and Load the Model 🔥
# 
# A model that exists only inside your Python session isn't useful in production.
# 
# Use:
# 
# import joblib
# 
# 
# joblib.dump(model, "student_model.pkl")
# 
# Then load it:
# 
# loaded_model = joblib.load("student_model.pkl")
# 
# Now:
# 
# prediction = loaded_model.predict(new_student)
# 
# This introduces an important production concept:
# 
# Train model
     # ↓
# Save model
     # ↓
# Later
     # ↓
# Load model
     # ↓
# Predict new data


import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


df=pd.read_csv("day35/Problem 5.csv")

print("\nFirst Five lines of Dataset :")
print(df.head())

print("\nShape of the Dataset :")
print(df.shape)

print("\nMissing Values of Dataset :")
print(df.isnull().sum())

print("\nDuplicate Rows :")
print(df.duplicated().sum())

print("\nBasic Information of the Dataset :")
df.info()

print("\nStatistical Information of the Dataset :")
print(df.describe())

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
        ("cat",OneHotEncoder(handle_unknown="ignore"),categorical_columns)
    ]
)

model=Pipeline([
    ("preprocessor",preprocessor),
    ("classsifier",LogisticRegression())
])

model.fit(X_train,y_train)

joblib.dump(model,"day35/student_model.pkl")

loaded_model=joblib.load("day35/student_model.pkl")

new_student = pd.DataFrame({
    "Age": [24],
    "Salary": [45000],
    "Experience": [2],
    "City": ["Hyderabad"],
    "Education": ["B.Tech"]
})


prediction=loaded_model.predict(new_student)
probability=loaded_model.predict_proba(new_student)

print("\nPrediction of New_Stuent is :")
print(prediction)

print("\nProbability Prediction of New_Stuent is :")
print(probability)