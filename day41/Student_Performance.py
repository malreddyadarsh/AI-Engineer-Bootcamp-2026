# 20. Mini Project
# Student Performance Prediction API
# 
# This is your first deployment-oriented ML project.
# 
# Architecture:
# 
# Student Data
      # ↓
# EDA
      # ↓
# Feature Engineering
      # ↓
# Preprocessing
      # ↓
# Model Training
      # ↓
# Hyperparameter Tuning
      # ↓
# Best Model
      # ↓
# Save Pipeline
      # ↓
# FastAPI
      # ↓
# POST /predict
      # ↓
# Prediction



import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV,StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from fastapi import FastAPI
from  pydantic import BaseModel
import joblib


# Student Data
data = {
    "Age": [
        18,19,20,21,22,19,20,18,21,22,
        20,19,21,18,22,20,19,21,18,22,
        20,21,19,18,22,20,19,21,18,22,
        19,20,21,22,18,19,20,21,22,18,
        20,19,21,22,18,20,21,19,22,18
    ],

    "Study_Hours": [
        2.0,3.0,5.0,6.0,7.0,2.5,4.5,1.5,5.5,7.5,
        4.0,3.5,6.0,2.0,8.0,5.0,3.0,6.5,1.0,7.0,
        4.5,5.5,2.5,3.0,8.0,6.0,4.0,7.0,2.0,6.5,
        3.5,5.0,6.5,7.5,1.5,3.0,4.5,6.0,7.0,2.5,
        5.5,4.0,6.0,8.0,2.0,5.0,7.0,3.5,8.0,1.5
    ],

    "Attendance": [
        65,70,82,88,92,68,78,60,85,94,
        80,74,87,64,96,83,71,90,58,91,
        79,84,69,73,95,86,77,89,62,88,
        75,81,93,97,59,67,76,85,90,70,
        83,78,92,98,61,80,87,72,94,57
    ],

    "Assignments_Completed": [
        5,6,8,9,10,6,8,4,9,10,
        8,7,9,5,10,9,6,10,3,9,
        8,9,6,7,10,9,8,10,5,9,
        7,8,10,10,4,6,7,9,10,6,
        8,7,9,10,5,8,10,6,10,4
    ],

    "Previous_Marks": [
        50,58,72,78,85,55,68,45,76,88,
        70,64,82,52,92,75,60,86,40,84,
        71,79,57,63,90,81,73,87,48,80,
        65,74,89,94,42,54,67,77,83,59,
        72,69,85,96,46,76,91,61,93,44
    ],

    "Gender": [
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female"
    ],

    "Study_Mode": [
        "Self","Coaching","Self","Coaching","Self",
        "Self","Coaching","Self","Coaching","Self",
        "Coaching","Self","Coaching","Self","Coaching",
        "Self","Coaching","Self","Coaching","Self",
        "Coaching","Self","Coaching","Self","Coaching",
        "Self","Coaching","Self","Coaching","Self",
        "Self","Coaching","Self","Coaching","Self",
        "Coaching","Self","Coaching","Self","Coaching",
        "Self","Coaching","Self","Coaching","Self",
        "Coaching","Self","Coaching","Self","Coaching"
    ],

    "Passed": [
        0,0,1,1,1,0,1,0,1,1,
        1,0,1,0,1,1,0,1,0,1,
        1,1,0,0,1,1,1,1,0,1,
        0,1,1,1,0,0,0,1,1,0,
        1,0,1,1,0,1,1,0,1,0
    ]
}

df = pd.DataFrame(data)


# EDA

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst Five rows of dataset :")
print(df.head())

print("\nMissing Values in the Dataset :")
print(df.isnull().sum())

print("\nDuplicate Rows in the Dataset :")
print(df.duplicated())

print("\nBasic Information of the Dataset :")
df.info()

print("\nStatistical Information of the Dataset :")
print(df.describe())

# Feature Engineering

df["Assignment_Rate"] = (
    df["Assignments_Completed"] / 10
) * 100

df.to_csv("Student.csv",index=False)

df=pd.read_csv("Student.csv")

numerical_columns=["Assignment_Rate","Age","Study_Hours","Attendance","Assignments_Completed","Previous_Marks"]

categorical_columns=["Gender","Study_Mode"]

X=df[["Assignment_Rate","Age","Study_Hours","Attendance","Assignments_Completed","Previous_Marks","Gender","Study_Mode"]]

y=df["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
preprocessor=ColumnTransformer(
    transformers=[
        ("cat",OneHotEncoder(),categorical_columns),
        ("num",StandardScaler(),numerical_columns)
    ]
)

pipeline=Pipeline([
    ("preprocessor",preprocessor),
    ("model",RandomForestClassifier(random_state=42))
])

cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
# Hyperparameter Tuning

param_grid={
    "model__n_estimators": [50, 100, 150],
    "model__max_depth": [None, 3, 5, 7],
    "model__min_samples_split": [2, 5],
    "model__min_samples_leaf": [1, 2],
    "model__max_features": ["sqrt", "log2"]
}

grid_search=GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=cv,
    scoring="f1",
    n_jobs=-1
)

grid_search.fit(X_train,y_train)

best_model=grid_search.best_estimator_

print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest CV Score:")
print(grid_search.best_score_)

joblib.dump(best_model,"Student_pipeline.pkl")


app=FastAPI()

loaded_model=joblib.load("Student_pipeline.pkl")

class StudentData(BaseModel):
    Age:int
    Study_Hours:float
    Attendance:int
    Assignments_Completed:int
    Previous_Marks:int
    Gender:str
    Study_Mode:str



@app.post("/predict")
def predict(data: StudentData):

    new_data=pd.DataFrame([data.model_dump()])

    # Feature Engineering
    new_data["Assignment_Rate"] = (
        new_data["Assignments_Completed"] / 10
    ) * 100

    prediction=loaded_model.predict(new_data)
    return {
        "Prediction":int(prediction[0])
    }