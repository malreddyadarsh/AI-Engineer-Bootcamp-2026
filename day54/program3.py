# Program 3 — Train a Model Using Batches

# Now we'll train:

# y = 2x

# but using a DataLoader.

import torch
import torch.nn as nn 
from torch.utils.data import TensorDataset,DataLoader

x=torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0]
])

y=torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0],
    [10.0],
    [12.0]
])

dataset=TensorDataset(x,y)

loader=DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

model=nn.Linear(1,1)

loss_fuction=nn.MSELoss()

optimizer=torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

epochs=100

for epoch in range(epochs):

    model.train()

    for batch_x,batch_y in loader :
        optimizer.zero_grad()

        prediction=model(batch_x)

        loss=loss_fuction(prediction,batch_y)

        loss.backward()

        optimizer.step()

        if epoch % 10 ==0 :

            print(
                f"Epoch :{epoch}",
                f"Loss  :{loss.item():.6f}"
            )

model.eval()

test=torch.tensor([[9.0]])

with torch.no_grad():
    prediction=model(test)

print("Predictin for 9 :",prediction.item())