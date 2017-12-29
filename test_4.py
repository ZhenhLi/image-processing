import numpy as np
import cv2

# 伪色彩变换
# OK

# The first way

image_1 = cv2.imread(r"C:\Data\project\4\1.jpg")
image_2 = cv2.imread(r"C:\Data\project\4\2.jpg")
image_3 = cv2.imread(r"C:\Data\project\4\3.jpg")
image_4 = cv2.imread(r"C:\Data\project\4\4.jpg")
print(image_1.shape)
cv2.imshow("image_1",image_1)
cv2.imshow("image_2",image_2)
cv2.imshow("image_3",image_3)
cv2.imshow("image_4",image_4)
cv2.waitKey()
cv2.destroyAllWindows()
# 调用applyColorMap()函数
image_1_color = cv2.applyColorMap(image_1,cv2.COLORMAP_AUTUMN)
image_2_color = cv2.applyColorMap(image_2,cv2.COLORMAP_HOT)
image_3_color = cv2.applyColorMap(image_3,cv2.COLORMAP_PINK)
image_4_color = cv2.applyColorMap(image_4,cv2.COLORMAP_SUMMER)

cv2.imshow("image_1_color",image_1_color)
cv2.imshow("image_2_color",image_2_color)
cv2.imshow("image_3_color",image_3_color)
cv2.imshow("image_4_color",image_4_color)
cv2.waitKey()
cv2.destroyAllWindows()

# Another way

# Note
# 0-f-63 : shape[0] = 0 ; shape[1] = 3*f; shape[2] = 255
# 64-127 : shape[0] = 0 ; shape[1] = 255; shape[2] = 255-
# 128-f-191: shape[0] = 0 ; shape[1] = 3*f; shape[2] = 255
# 192-f-255: shape[0] = 0 ; shape[1] = 3*f; shape[2] = 255
image_1_hsv = cv2.cvtColor(image_1,cv2.COLOR_RGB2HSV)

def function(image):
    image_re = np.zeros(image.shape)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if 0 <= image[i,j,0] <= 63:
                image_re[i,j,2] = 4 * image.shape[0]
                image_re[i,j,1] = 255
                image_re[i,j,0] = 0
            elif 64 < image[i,j,0] <= 127:
                image_re[i,j,2] = 255
                image_re[i,j,1] = 255
                image_re[i,j,0] = 4 * (image.shape[0] - 64)
            elif 128 < image[i,j,0] <= 191:
                image_re[i,j,2] = 255
                image_re[i,j,1] = 255 - 4 * (image.shape[0] - 128)
                image_re[i,j,0] = 255
            elif 192 < image[i,j,0] <= 255:
                image_re[i,j,2] = 255 - 4 * (image.shape[0] - 192)
                image_re[i,j,1] = 0
                image_re[i,j,0] = 255
    return image_re

image_1_result = function(image_1)
cv2.imshow("image_1_result",image_1_result)
cv2.waitKey()
cv2.destroyAllWindows()