# Program 4 — Save & Load
# 
# After training:
# 
# Save:
# student_regressor.pth
# student_scaler.pkl
# 
# Then create a separate:
# 
# predict.py
# 
# Load both and make a prediction for a new student.
# 
# Verify that the loaded model produces the same result as the original trained model for the same input.


# AFTER TRAINING THE MODEL , THE REGRESSOR MODEL & SCALER ARE SAVED IN THE day56/program4.py.

import joblib
import torch
import torch.nn as nn
import numpy as np

class StudentRegressor(nn.Module):

    def __init__(self):

        super().__init__()

        self.layer1=nn.Linear(3,8)

        self.layer2=nn.Linear(8,4)

        self.output=nn.Linear(4,1)

        self.relu=nn.ReLU()

    def forward(self,x):

        x=self.layer1(x)
        x=self.relu(x)

        x=self.layer2(x)
        x=self.relu(x)

        x=self.output(x)

        return x

# Loading Scaler

scaler=joblib.load("day56/student_scaler.pkl")

# Loading Model

model=StudentRegressor()

model.load_state_dict(torch.load(
    "day56/student_regressor.pth",))

model.eval()

new_student=np.array([[5.6,60.5,62.8]],dtype=np.float32)

# Scale
new_student_scaled=scaler.transform(new_student)

# Convert to Tensors

x=torch.tensor(new_student_scaled,dtype=torch.float32)

# Prediction

with torch.no_grad():

    prediction=model(x)

print("Predicted Marks are :",prediction)