import torch 
import torch.nn as nn

actual = [10, 20, 30]
prediction = [8, 18, 33]

actual=torch.tensor([
    [10.0],
    [20.0],
    [30.0]
])

prediction=torch.tensor([
    [8.0],
    [18.0],
    [33.0]
])

loss_fuction=nn.MSELoss()

loss=loss_fuction(prediction,actual)

print("Loss is :",loss)