import torch 
import torch.nn as nn
import numpy as np
import joblib

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

scaler=joblib.load("day56/Student_Scaler1.pkl")

# Loading Model

model=StudentRegressor()

model.load_state_dict(torch.load(
    "day56/Student_Regressor1.pth"
))

# Model Evaluation

model.eval()

new_student=np.array([[4.9,85.2,85.2]],dtype=np.float32)

# Scaling New Student

new_student_scaled=scaler.transform(new_student)

# Converting To Tensors

new=torch.tensor(new_student_scaled,dtype=torch.float32)

# Prediction

with torch.no_grad():

    prediction=model(new)

print("Prediction of Marks :",prediction)