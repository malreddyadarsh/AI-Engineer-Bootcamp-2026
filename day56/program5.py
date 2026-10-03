# Program 5 — Full ML Engineering Challenge
# 
# Build this without copying the complete solution:
# 
# train.py
# │
# ├── Load data
# ├── Split data
# ├── Scale data
# ├── Tensor conversion
# ├── DataLoader
# ├── Define model
# ├── Train
# ├── Evaluate
# ├── Print MAE/MSE/RMSE/R²
# ├── Save model
# └── Save scaler
# 
# Then:
# 
# predict.py
# │
# ├── Load scaler
# ├── Load model
# ├── Accept new student data
# ├── Scale input
# ├── Convert to tensor
# └── Predict marks


import numpy as np
import torch
import torch.nn as nn
import joblib
from torch.utils.data import TensorDataset,DataLoader

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# Load data

X = np.array([
    [1.5, 62.0, 55.0],
    [2.0, 68.0, 60.0],
    [2.5, 72.0, 64.0],
    [3.0, 76.0, 68.0],
    [3.5, 80.0, 72.0],
    [4.0, 84.0, 76.0],
    [4.5, 88.0, 80.0],
    [5.0, 91.0, 84.0],
    [5.5, 94.0, 88.0],
    [6.0, 96.0, 91.0],
    [1.0, 58.0, 50.0],
    [2.2, 70.0, 63.0],
    [3.2, 78.0, 70.0],
    [4.2, 86.0, 77.0],
    [5.2, 92.0, 85.0]
],dtype=np.float32)

y =np.array([
    52.0,
    58.0,
    63.0,
    68.0,
    73.0,
    78.0,
    83.0,
    88.0,
    93.0,
    96.0,
    47.0,
    61.0,
    71.0,
    79.0,
    86.0
],dtype=np.float32)

# Split data

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
    )

# Scale data

scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)

X_test=scaler.transform(X_test)

# Tensor conversion

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
    dtype=torch.float32
).reshape(-1,1)

# DataLoader

train_dataset=TensorDataset(
    X_train,
    y_train
)

train_dataloader=DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True
)

# Define model

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
    lr=0.01
)

# Training

epochs=100

for epoch in range(epochs):

    model.train()

    total_loss=0

    for batch_x,batch_y in train_dataloader:

        optimizer.zero_grad()

        prediction=model(batch_x)

        loss=loss_function(prediction,batch_y)

        loss.backward()

        optimizer.step()

        total_loss+=loss.item()

    average_loss=total_loss/(len(train_dataloader))

    if epoch % 50 == 0:

        print(
            f"Epoch :{epoch}",
            f"Loss  :{average_loss:.4f}"
        )

# Model Evaluation

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

print("MAE :",mae)
print("MSE :",mse)
print("RMSE :",rmse)
print("R2 Score :",r2)

torch.save(
    model.state_dict(),
        "day56/Student_Regressor1.pth"
)

joblib.dump(scaler,"day56/Student_Scaler1.pkl")

# For next part Check-in into day56/program5(predict).py

