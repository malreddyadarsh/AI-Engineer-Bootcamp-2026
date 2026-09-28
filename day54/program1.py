# Program 1 — Custom Dataset

import torch
from torch.utils.data import Dataset

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

print("\nSize Of The Dataset :",len(dataset))

for i in range (len(dataset)):
    x,y=dataset[i]

    print("Input  :",x)
    print("Output :",y)
    print("\n")