# Program 3 — Student Classification
# 
# Train the model using:
# 
# Study Hours
# Attendance
# Previous Marks
# 
# Target:
# 
# 0 = Fail
# 1 = Pass
# 
# Use:
# 
# StandardScaler
# TensorDataset
# DataLoader
# BCEWithLogitsLoss
# Adam

import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset,DataLoader

from sklearn.model_selection import 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,recall_score,precision_score


df=pd.read_csv("day55/student.csv")

print(df.head())

X=df[["Study_Hours","Attendance","Previous_Marks"]].values

y=df["Passed"].values

scaler=StandardScaler()

X=scaler.fit_transform(X)

# Convert dataset values to Tensors

X_tensor=torch.tensor(
    X,
    dtype=torch.float32
)

y_tensor=torch.tensor(
    y,
    dtype=torch.float32
).reshape(-1,1)

# Tensor Dataset

dataset=TensorDataset(X_tensor,y_tensor)

# DataLoader

dataloader=DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

# Modeling

class BinarClassifier(nn.Module):

    def __init__(self):

        super().__init__()

        self.layer1=nn.Linear(3,8)
        self.relu1=nn.ReLU()

        self.layer2=nn.Linear(8,4)
        self.relu2=nn.ReLU()

        self.output=nn.Linear(4,1)

    def forward(self,x):

        x=self.layer1(x)
        x=self.relu1(x)

        x=self.layer2(x)
        x=self.relu2(x)

        x=self.output(x)

        return x

model=BinarClassifier()

loss_function=nn.BCEWithLogitsLoss()

optimizer=torch.optim.Adam(
    model.parameters(),
    lr=.001
)

epochs=100

for epoch in range(epochs):

    model.train()

    total_loss=0

    for X_batch,y_batch in dataloader:

        optimizer.zero_grad()

        output=model(X_batch)
        
        loss=loss_function(output,y_batch)

        loss.backward()

        optimizer.step()

        if (epoch +1 ) % 10 ==0 :
            print(
                f"Epoch :{epoch}",
                f"Loss  :{total_loss/(len(dataset)):.4f}"
            )

# Evalvation

model.eval()
with torch.no_grad():

    logits=model(X_tensor)
    probabilities=torch.sigmoid(logits)
    prediction=(probabilities>=0.5).float()

# Convert to tensors 

y_true=y_tensor.numpy().flatten()

y_pred=prediction.numpy().flatten()


# Program 4 — Classification Metrics

# After training, calculate:

# Accuracy
# Confusion Matrix
# Precision
# Recall

# Use:

# sklearn.metrics

print(f"Accuracy Score :{accuracy_score(y_true,y_pred)}")

print(f"Confusion Matrix :{confusion_matrix(y_true,y_pred)}")

print(f"Precision Score :{precision_score(y_true,y_pred)}")

print(f"Recall Score :{recall_score(y_true,y_pred)}")
