#-*-coding:UTF-8-*-
import cv2
import matplotlib.pyplot as plt


#彩色图像使用 OpenCV 加载时是 BGR 模式。但是 Matplotib 是 RGB模式。
#所以彩色图像如果已经被 OpenCV 读取，那它将不会被 Matplotib 正确显示。
#Matplotlib是RGB，而Opnecv是BGR，所以我们需要先将Opencv读入的彩色图像拆分成B、G、R三个通道，然后再按R、G、B顺序合并三个通道

img = cv2.imread('cat.jpg')
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])

plt.subplot(121)
plt.title('bgr')
plt.imshow(img)
plt.subplot(122)
plt.title('rgb')
plt.imshow(img2)
plt.show()
