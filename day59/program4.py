# Task 4 — Build both regressors
# Create StudentRegressorBN and StudentRegressorLN; verify output shapes.

import torch
import torch.nn as nn

class StudentRegressorBN(nn.Module):

    def __init__(self):

        super().__init__()

        self.layer1=nn.Linear(3,16)
        self.bn1=nn.BatchNorm1d(16)
        self.relu=nn.ReLU()

        self.layer2=nn.Linear(16,8)
        self.bn2=nn.BatchNorm1d(8)

        self.output=nn.Linear(8,1)

    def forward(self,x):

        x=self.layer1(x)
        x=self.bn1(x)
        x=self.relu(x)

        x=self.layer2(x)
        x=self.bn2(x)
        x=self.relu(x)

        x=self.output(x)
        return x

class StudentRegressorLN(nn.Module):

    def __init__(self):

        super().__init__()

        self.layer1=nn.Linear(3,16)
        self.ln1=nn.LayerNorm(16)
        self.relu=nn.ReLU()

        self.layer2=nn.Linear(16,8)
        self.ln2=nn.LayerNorm(8)

        self.output=nn.Linear(8,1)

    def forward(self,x):

        x=self.layer1(x)
        x=self.ln1(x)
        x=self.relu(x)

        x=self.layer2(x)
        x=self.ln2(x)
        x=self.relu(x)

        x=self.output(x)

        return x


model_bn=StudentRegressorBN()

model_ln=StudentRegressorLN()

X=torch.randn(5,3)

print("\nInput :")
print(X)

# Model Evaluation

model_bn.eval()
model_ln.eval()

with torch.no_grad():

    output_bn=model_bn(X)
    output_ln=model_ln(X)

print("Input Shape :",X.shape)
print("Batch Norm Output Shape :",output_bn.shape)
print("Layer Norm Output Shape :",output_ln.shape)

print("\nBatch Norm Prediction is :\n",output_bn)
print("\nLayer Norm Prediction is :\n",output_ln)