import torch
import torch.nn as nn
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader,TensorDataset
import matplotlib.pyplot as plt

X = np.array([
    [2,55,40],
    [3,60,45],
    [4,65,50],
    [5,70,58],
    [6,75,62],
    [7,80,70],
    [8,85,75],
    [9,90,82],
    [10,95,88],
    [3,58,43],
    [4,68,53],
    [6,78,66],
    [7,83,72],
    [8,88,78],
    [9,92,85],
    [5,72,60]
], dtype=np.float32)


y = np.array([
    42,47,55,62,
    68,75,81,87,
    94,45,57,71,
    77,83,91,64
], dtype=np.float32)

# SPLITTING DATA 

X_train,X_temp,y_train,y_temp=train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

X_val,X_test,y_val,y_test=train_test_split(
    X_temp,
    y_temp,
    test_size=0.5,
    random_state=42
)

# SCALE THE DATA

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)

X_val=scaler.transform(X_val)

X_test=scaler.transform(X_test)


# CONVERT TO TENSORS

X_train=torch.tensor(
    X_train,
    dtype=torch.float32
)

X_val=torch.tensor(
    X_val,
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

y_val=torch.tensor(
    y_val,
    dtype=torch.float32
).reshape(-1,1)

y_test=torch.tensor(
    y_test,
    dtype=torch.float32
).reshape(-1,1)


class LargeStudentModel(nn.Module):

    def __init__(self):
          super().__init__()

          self.layer1=nn.Linear(3,128)
          self.layer2=nn.Linear(128,128)
          self.layer3=nn.Linear(128,64)
          self.layer4=nn.Linear(64,32)

          self.relu=nn.ReLU()

          self.dropout=nn.Dropout(0.3)

          self.output=nn.Linear(32,1)

    def forward(self,x):

         x=self.layer1(x)
         x=self.relu(x)
         x=self.dropout(x)

         x=self.layer2(x)
         x=self.relu(x)
         x=self.dropout(x)

         x=self.layer3(x)
         x=self.relu(x)
         x=self.dropout(x)

         x=self.layer4(x)
         x=self.relu(x)
         x=self.dropout(x)

         x=self.output(x)

         return x

model=LargeStudentModel()

loss_function=nn.MSELoss()

optimizer=torch.optim.Adam(
     model.parameters(),
     lr=0.001,
     weight_decay=1e-4
)


# train_losses=[]
# val_losses=[]


# for epoch in range(1000):

     # # TRAINING

     # model.train()

     # optimizer.zero_grad()

     # train_prediction=model(X_train)

     # train_loss=loss_function(
          # train_prediction,y_train
     # )

     # train_loss.backward()

     # optimizer.step()


     # # VALIDATION

     # model.eval()

     # with torch.no_grad():

          # val_prediction=model(X_val)

          # val_loss=loss_function(
               # val_prediction,y_val
          # )

     # train_losses.append(train_loss.item())
     # val_losses.append(val_loss.item())

     # if epoch % 100 == 0:

          # print(
               # f"EPOCH :{epoch}",
               # f"TRAIN LOSSES :{train_losses[-1]:.4f}",
               # f"VAL LOSSES :{val_losses[-1]:.4f}"
          # )

# plt.plot(train_losses,label="Training Loss")
# plt.plot(val_losses,label="Validation Loss")

# plt.xlabel("Epoch")
# plt.ylabel("Loss")

# plt.title("Training VS Validation Losses")

# plt.legend()

# plt.show()


best_val_loss=float("inf")

patience=10

counter=0

for epoch in range(1000):

     model.train()

     optimizer.zero_grad()

     train_prediction=model(X_train)

     train_loss=loss_function(
          train_prediction,y_train
     )

     train_loss.backward()

     optimizer.step()

     model.eval()

     with torch.no_grad():

          val_prediction=model(X_val)

          val_loss=loss_function(
               val_prediction,y_val
          ).item()
     if val_loss < best_val_loss:

          best_val_loss=val_loss

          counter=0

          torch.save(
               model.state_dict(),
               "day57/best_student_model.pth"
          )
     else :

          counter+=1

     if counter <= patience:

          print("Early Stopping at Epoch :",epoch)
          break

model.load_state_dict(
     torch.load(
          "day57/best_student_model.pth"
     )
)

with torch.no_grad():

     test_prediction=model(X_test)

     test_loss=loss_function(
          test_prediction,y_test
     ).item()

print(f"LOSS OF TEST SET IS :{test_loss:.4f}")