# Program 1 — Save and Load a Model

# Use your best model from Day 40.

# Do:

# Train
 # ↓
# Save using joblib
 # ↓
# Close/restart Python
 # ↓
# Load model
 # ↓
# Predict

# You should demonstrate that the loaded model gives the same prediction as before.

import joblib
import pandas as pd

model=joblib.load("Student_DT_model.pkl")

new_data=pd.DataFrame({
    "Age":[19],
    "Study_Hours":[6],
    "Attendance":[85],
    "Assignments_Completed":[6],
    "Previous_Marks":[70]
})

prediction=model.predict(new_data)

print("\nPrediction on NewData is :")
print(prediction)