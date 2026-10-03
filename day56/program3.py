# Program 3 — Student Marks Neural Network
# 
# Build:
# 
# 3 features
 # ↓
# 8
 # ↓
# ReLU
 # ↓
# 4
 # ↓
# ReLU
 # ↓
# 1
# 
# Train it to predict marks.
# 
# Use:
# 
# MSELoss
# Adam
# DataLoader


import numpy as np
import torch
import torch.nn as nn
import joblib
from torch.utils.data import DataLoader,TensorDataset

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

X = np.array([
    [2.0, 70.0, 60.0],
    [3.0, 75.0, 65.0],
    [4.0, 80.0, 70.0],
    [5.0, 85.0, 75.0],
    [6.0, 90.0, 80.0],
    [1.0, 60.0, 50.0],
    [2.5, 68.0, 58.0],
    [3.5, 78.0, 68.0],
    [4.5, 82.0, 72.0],
    [5.5, 88.0, 78.0],
    [6.5, 92.0, 85.0],
    [1.5, 65.0, 55.0]
], dtype=np.float32)

y = np.array([
    58.0,
    65.0,
    72.0,
    78.0,
    85.0,
    48.0,
    56.0,
    68.0,
    75.0,
    82.0,
    90.0,
    52.0
],dtype=np.float32)

# Splitting DataSet 

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.5,
    random_state=42
)

scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)

X_test=scaler.transform(X_test)

# Convert to Tensors

X_train=torch.tensor(
    X_train,
    dtype=torch.float32
)

X_test=torch.tensor(
    X_test,
    dtype=torch.float32
)

y_train=torch.tensor(
    y_train,
    dtype=torch.float32
).reshape(-1,1)

y_test=torch.tensor(
    y_test,
    dtype=torch.float32,
).reshape(-1,1)

train_dataset=TensorDataset(
    X_train,
    y_train
)

train_dataloader=DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True
)

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

model=StudentRegressor()

loss_function=nn.MSELoss()

optimizer=torch.optim.Adam(
    model.parameters(),
    lr=.01
)

epochs=100

for epoch in range(epochs):

    model.train()

    total_loss=0

    for batch_x,batch_y in train_dataloader:
        optimizer.zero_grad()
        
        prediction=model(batch_x)

        loss=loss_function(
            prediction,batch_y
        )

        loss.backward()

        optimizer.step()

        total_loss+=loss.item()

    average_loss=(total_loss)/(len(train_dataset))

    if epoch % 50 == 0:

        print(
            f"Epoch :{epoch}",
            f"Loss  :{average_loss:.4f}"
            )


model.eval()

with torch.no_grad():

    prediction=model(X_test)

actual=y_test.numpy().flatten()
predicted=prediction.numpy().flatten()

mae=mean_absolute_error(
    actual,predicted
)

mse=mean_squared_error(
    actual,predicted
)

rmse=np.sqrt(mse)

r2=r2_score(
    actual,predicted
)

print("MAE  :",mae)

print("MSE  :",mse)

print("RMSE :",rmse)

print("R2_Score :",r2)


torch.save(model.state_dict(),
           "day56/student_regressor.pth")

joblib.dump(scaler,"day56/student_scaler.pkl")