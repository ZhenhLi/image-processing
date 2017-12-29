import numpy as np
import cv2

# 提取黑框中文字
# OK

image = cv2.imread(r"C:\Data\project\2\text2.tif")
cv2.imshow("image",image)
cv2.waitKey()
cv2.destroyAllWindows()

image_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
equ = cv2.equalizeHist(image_gray)
image_gray_not = cv2.bitwise_not(image_gray)
retval, image_thre = cv2.threshold(image_gray_not,175,255,cv2.THRESH_BINARY)

print(retval)
cv2.imshow("equ",equ)
cv2.imshow("image_gray",image_gray)
cv2.imshow("image_gray_not",image_gray_not)
cv2.imshow("image_thre",image_thre)
cv2.waitKey()
cv2.destroyAllWindows()

image_gray_not_2 = image_gray_not.copy()
mask = np.zeros(image_gray.shape,np.uint8)

image_contours,contours, hierarchy = cv2.findContours(image_thre,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(image_gray_not,[cnt],0,(0,0,0),2)
    cv2.drawContours(mask,[cnt],0,255,-1)
# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#         if image_gray_not_2[i,j] < 220:
#             image_gray_not_2[i,j] = 0
cv2.imshow("image_gray",image_gray_not)
cv2.imshow("mask",mask)
cv2.imshow("image_contours",image_contours)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.bitwise_not(image_gray_not_2,image_gray_not_2,mask)
image_gray_not_not = cv2.bitwise_not(image_gray_not_2)
cv2.imshow("image_gray_2",image_gray_not_2)
cv2.imshow("image_gray_not_not",image_gray_not_not)
cv2.waitKey()
cv2.destroyAllWindows()
image_equ = cv2.equalizeHist(image_gray_not_not)
image_equ_1 = cv2.equalizeHist(image_gray_not_2)
image_gray_not_equ_not = cv2.bitwise_not(image_equ_1)
cv2.imshow("image_equ_1",image_equ_1)
cv2.imshow("image_equ_1_not",image_gray_not_equ_not)
cv2.imshow("image_equ",image_equ)
cv2.waitKey()
cv2.destroyAllWindows()