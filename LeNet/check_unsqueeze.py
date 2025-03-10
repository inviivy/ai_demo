import torch

t = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(t.shape)
t2 = torch.unsqueeze(t, dim=0)
print(t2.shape)
print(t2)
t3 = torch.unsqueeze(t, dim=1)
print(t3.shape)
print(t3)