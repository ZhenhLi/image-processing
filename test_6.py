import numpy as np
import cv2

# Project 6 提取白块
# 没有思路

image_1 = cv2.imread(r"C:\Data\project\6\Fig4.jpg")
image_2 = cv2.imread(r"C:\Data\project\6\pvm2.jpg")

cv2.imshow("image_1",image_1)
cv2.imshow("image_2",image_2)
# cv2.waitKey()
# cv2.destroyAllWindows()

for i in range(image_1.shape[0]):
    for j in range(image_1.shape[1]):
        if image_1[i,j,0] >= 170:
            image_1[i,j] = 255
        else:
            image_1[i,j] = 0

cv2.imshow("image_1_new",image_1)
cv2.waitKey()
cv2.destroyAllWindows()
kernel_3x3 = np.array([[-1,-1,-1],
                       [-1,8,-1],
                       [-1,-1,-1]])
image_erode = cv2.erode(image_1,kernel_3x3)
