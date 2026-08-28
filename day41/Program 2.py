# Program 2 — Save the Complete Pipeline 🔥

# Create:

# Numerical features
# Categorical features

# Build:

# ColumnTransformer
      # ↓
# Model
      # ↓
# Pipeline

# Then:

# joblib.dump(
    # pipeline,
    # "student_pipeline.pkl"
# )

# Load:

# loaded_pipeline = joblib.load(
    # "student_pipeline.pkl"
# )

# Then predict a new student.

# Goal

# Prove that you don't need to manually preprocess the new student.






import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

data = {

    "Age": [
        18,19,18,20,21,19,20,22,18,21,
        19,20,18,22,21,19,20,18,22,21,
        20,19,18,22,21,19,20,18,22,21
    ],

    "Study_Hours": [
        2.0,3.0,4.0,5.0,6.0,2.5,4.5,7.0,1.5,5.5,
        3.5,6.0,2.0,8.0,4.0,2.5,5.0,3.0,7.5,3.5,
        6.5,2.0,4.5,8.0,5.0,3.0,6.0,1.0,7.0,4.0
    ],

    "Attendance": [
        65,70,75,80,85,68,78,90,60,82,
        72,88,64,92,76,66,81,71,91,73,
        86,63,77,94,80,69,84,58,89,74
    ],

    "Assignments_Completed": [
        6,7,8,9,9,6,8,10,5,9,
        7,10,6,10,8,6,9,7,10,7,
        9,5,8,10,9,7,9,4,10,8
    ],

    "Previous_Marks": [
        55,62,68,72,78,58,70,85,50,75,
        64,80,53,88,69,57,74,61,87,65,
        82,52,71,90,76,60,79,48,84,67
    ],

    # Categorical Feature 1
    "Gender": [
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female"
    ],

    # Categorical Feature 2
    "Study_Mode": [
        "Self","Coaching","Self","Coaching","Self",
        "Self","Coaching","Self","Self","Coaching",
        "Self","Coaching","Self","Coaching","Self",
        "Self","Coaching","Self","Coaching","Self",
        "Coaching","Self","Coaching","Self","Coaching",
        "Self","Coaching","Self","Coaching","Self"
    ],

    "Passed": [
        0,0,1,1,1,0,1,1,0,1,
        0,1,0,1,1,0,1,0,1,0,
        1,0,1,1,1,0,1,0,1,0
    ]
}

df = pd.DataFrame(data)

categorical_features=["Gender","Study_Mode"]

numerical_features=["Age","Study_Hours","Attendance","Assignments_Completed","Previous_Marks"]

X=df[["Age","Study_Hours","Attendance","Assignments_Completed","Previous_Marks","Gender","Study_Mode"]]

y=df["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

preprocessor=ColumnTransformer(
    transformers=[
        ("cat",OneHotEncoder(),categorical_features),
        ("num",StandardScaler(),numerical_features)
    ]
)

pipeline=Pipeline([
    ("preprocessor",preprocessor),
    ("model",LogisticRegression())
])

pipeline.fit(X_train,y_train)

prediction=pipeline.predict(X_test)

joblib.dump(pipeline,"student_pipeline.pkl")

loaded_pipeline=joblib.load("student_pipeline.pkl")

new_data = pd.DataFrame({
    "Age": [20],
    "Study_Hours": [6.5],
    "Attendance": [88],
    "Assignments_Completed": [9],
    "Previous_Marks": [78],
    "Gender": ["Male"],
    "Study_Mode": ["Coaching"]
})

print("\nNew Prediction Data :")
print(new_data)

predictions=loaded_pipeline.predict(new_data)

print("\nPrediction :")
print(predictions)