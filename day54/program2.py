# Program 2 — DataLoader

import torch
from torch.utils.data import Dataset,DataLoader

class StudentDataset(Dataset):

    def __init__(self):

        self.x=torch.tensor([
            [7.0, 90.0],
            [3.0, 60.0],
            [8.0, 95.0],
            [4.0, 70.0],
            [6.0, 85.0]
        ])

        self.y=torch.tensor([
            [1.0],
            [0.0],
            [1.0],
            [0.0],
            [1.0]
        ])

    def __len__(self):
        return len(self.x)

    def __getitem__(self,index):
        return self.x[index], self.y[index]


dataset=StudentDataset()

loader=DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

for batch_x,batch_y in loader:

    print("Batch X :")
    print(batch_x)

    print("Batch Y :")
    print(batch_y)

    print("X Shape :",batch_x.shape)
    print("Y Shape :",batch_y.shape)

    print("--------------------------------")