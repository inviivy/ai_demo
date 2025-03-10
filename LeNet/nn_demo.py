import torch
import torch.nn as nn

im = torch.randn(1, 1, 5, 5)
c = nn.Conv2d(1, 1, kernel_size=3, stride=1, padding=2, dilation=2)
output = c(im)

print("Input shape:", im.shape)
print("Output shape:", output.shape)