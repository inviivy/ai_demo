import torchvision.transforms as transforms
from PIL import Image
import numpy as np

# 创建一个全白的像素数值为255的3*3图像
dummy_image = Image.fromarray(np.ones((3, 8, 4), dtype=np.uint8) * 255)
tensor_image = transforms.ToTensor()(dummy_image)

print("原始像素值(PIL):", np.array(dummy_image))
print("转换后张量值:", tensor_image)
print("张量形状:", tensor_image.shape)


# 理解这里的shape就行
x = np.ones((3, 5), dtype=np.uint8)
print(x)
print(x.shape)