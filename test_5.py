import numpy as np
import cv2

# 提取眼中血管
# OK

image_1 = cv2.imread(r"C:\Data\project\5\pic1.png")
image_2 = cv2.imread(r"C:\Data\project\5\pic2.png")
image_3 = cv2.imread(r"C:\Data\project\5\pic3.png")
image_4 = cv2.imread(r"C:\Data\project\5\pic4.png")

cv2.imshow("image_1",image_1)
cv2.imshow("image_2",image_2)
cv2.imshow("image_3",image_3)
cv2.imshow("image_4",image_4)
cv2.waitKey()
cv2.destroyAllWindows()

image_1_gray = cv2.cvtColor(image_1,cv2.COLOR_RGB2GRAY)
image_2_gray = cv2.cvtColor(image_2,cv2.COLOR_RGB2GRAY)
image_3_gray = cv2.cvtColor(image_3,cv2.COLOR_RGB2GRAY)
image_4_gray = cv2.cvtColor(image_4,cv2.COLOR_RGB2GRAY)

cv2.imshow("image_1_gray",image_1_gray)
cv2.imshow("image_2_gray",image_2_gray)
cv2.imshow("image_3_gray",image_3_gray)
cv2.imshow("image_4_gray",image_4_gray)
cv2.waitKey()
cv2.destroyAllWindows()

image_1_mean = cv2.adaptiveThreshold(image_4_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,13,7)
retval, image_1_m = cv2.threshold(image_4_gray,150,255,cv2.THRESH_BINARY)
cv2.imshow("image_4_mean",image_1_mean)
cv2.imshow("image_4_m",image_1_m)
cv2.waitKey()
cv2.destroyAllWindows()