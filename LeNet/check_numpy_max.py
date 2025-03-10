import torch

import numpy as np

x = np.random.randint(0, 256, size=(3,4,5),dtype=np.uint8)
print(x)

tensor = torch.from_numpy(x)
print(f'dim=0: {torch.max(tensor, dim=0)}')
print(f'dim=1: {torch.max(tensor, dim=1)}')
print(f'dim=2: {torch.max(tensor, dim=2)}')
