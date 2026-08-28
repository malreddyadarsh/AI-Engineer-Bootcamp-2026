# Program 4 — Prediction API 🔥
# 
# Create:
# 
# POST /predict
# 
# Request:
# 
#"Age":[19],
# "Study_Hours":[6],
# "Attendance":[85],
# "Assignments_Completed":[6],
# "Previous_Marks":[70]
#  
#
# 
# The API should:
# 
# Receive data
 # ↓
# Validate
 # ↓
# Create DataFrame
 # ↓
# Load saved model
 # ↓
# Predict
 # ↓
# Return JSON
# 
# Response:
# 
# {
  # "prediction": 1
# }

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app=FastAPI()

model=joblib.load("Student_DT_model.pkl")

class StudentData(BaseModel):
    Age:float
    Study_Hours:float
    Attendance:float
    Assignments_Completed:float
    Previous_Marks:float


@app.post("/predict")
def predict(data: StudentData):
    # Convert validated data into DataFrame
    new_data = pd.DataFrame([data.model_dump()])

    # Make prediction
    prediction = model.predict(new_data)
    probability=model.predict_proba(new_data)[0][1]

    # Return prediction as JSON
    return {
        "prediction": int(prediction[0]),
        "probability":float(probability)
    }



# Program 5 — Prediction Probability API 🔥

# Extend Program 4.

# Return:

# {
  # "prediction": 1,
  # "probability": 0.93
# }

# For example:

# probability = model.predict_proba(data)[0][1]

# Then:

# return {
    # "prediction": int(prediction),
    # "probability": float(probability)
# }