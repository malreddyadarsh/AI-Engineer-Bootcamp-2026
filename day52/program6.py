# Program 6 — Device Check

import torch

device=torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

x=torch.tensor([1.0,3.9]).to(device)

print(x.device)