import torch 
import torch.nn as nn

x=torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

y=torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0],
    [10.0]
])

model=nn.Linear(1,1)

loss_function=nn.MSELoss()

optimizer=torch.optim.SGD(model.parameters(),lr=0.01)

for epoch in range(1000):

    optimizer.zero_grad()

    prediction=model(x)

    loss=loss_function(prediction,y)

    loss.backward()

    optimizer.step()

    if epoch % 100 ==0:
        print(f"Epoch : {epoch}",
              f"Loss :{loss.item():.6f}")

print("Weight is :")
print(model.weight.item())

print("Weight is :")
print(model.bias.item())

test=torch.tensor([[6.0]])

prediction=model(test)

print("Prediction for 6 is :",prediction.item())