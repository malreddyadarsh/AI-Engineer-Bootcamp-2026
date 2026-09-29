import torch
import numpy as np

import torch.nn as nn
from torch.utils.data import DataLoader,TensorDataset

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix

X = np.array([
    [2, 55, 45],
    [3, 60, 50],
    [4, 65, 55],
    [5, 70, 60],
    [6, 72, 62],
    [7, 75, 65],
    [8, 80, 70],
    [9, 85, 75],
    [10, 90, 82],
    [1, 50, 40],
    [2, 58, 48],
    [3, 62, 52],
    [4, 68, 57],
    [5, 74, 63],
    [6, 78, 67],
    [7, 82, 72],
    [8, 86, 76],
    [9, 88, 80],
    [10, 92, 85],
    [2, 52, 43],
    [3, 59, 49],
    [4, 64, 54],
    [5, 69, 58],
    [6, 73, 64],
    [7, 77, 68],
    [8, 81, 73],
    [9, 84, 78],
    [10, 91, 84],
    [1, 48, 38],
    [3, 61, 51],
    [4, 67, 56],
    [5, 71, 61],
    [6, 76, 66],
    [7, 79, 70],
    [8, 83, 74],
    [9, 87, 79],
    [10, 94, 88],
    [2, 57, 46],
    [3, 63, 53],
    [4, 66, 59],
    [5, 72, 62],
    [6, 75, 65],
    [7, 80, 71],
    [8, 85, 77],
    [9, 89, 81],
    [10, 95, 90]
], dtype=np.float32)


y = np.array([
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1
], dtype=np.float32)


X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

scalar=StandardScaler()

X_train=scalar.fit_transform(X_train)

X_test=scalar.transform(X_test)

# Convert to tensors

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

train_dataset=TensorDataset(
    X_train,
    y_train
    )

train_loader=DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True
)

class StudentClassifier(nn.Module):

    def __init__(self):
        super().__init__()

        self.layer1=nn.Linear(3,8)

        self.layer2=nn.Linear(8,4)
        
        self.relu=nn.ReLU()

        self.output=nn.Linear(4,1)

    def forward(self,x):

        x=self.layer1(x)
        x=self.relu(x)

        x=self.layer2(x)
        x=self.relu(x)

        x=self.output(x)

        return x

model=StudentClassifier()

loss_function=nn.BCEWithLogitsLoss()

optimizer=torch.optim.Adam(
    model.parameters(),
    lr=0.01
)

# Training

epochs=100

for epoch in range(epochs):

    model.train()

    total_loss=0

    for batch_x,batch_y in train_loader:

        optimizer.zero_grad()

        logits=model(batch_x)

        loss=loss_function(logits,batch_y)

        loss.backward()

        optimizer.step()

        total_loss+=loss.item()

    average_loss=(total_loss/len(train_dataset))
    if epoch % 10 == 0:
        print(
            f"Epoch :{epoch}",
            f"Loss  :{average_loss:.4f}"
        )

# Evaluation

model.eval()

with torch.no_grad():

    logits=model(X_test)
    probabilities=torch.sigmoid(logits)

    predictions=(
        probabilities >=.5
    ).float()


y_true=y_test.numpy().flatten()

y_pred=predictions.numpy().flatten()

print(f"\nAccuracy Score   :{accuracy_score(y_true,y_pred):.2f}")

print(f"\nConfusion Matrix :{confusion_matrix(y_true,y_pred)}")

print(f"\nPrecision Score  :{precision_score(y_true,y_pred):.2f}")

print(f"\nRecall Score     :{recall_score(y_true,y_pred):.2f}")