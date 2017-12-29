import numpy as np
import cv2

image = np.zeros((200,200),dtype=np.uint8)
image[50:150,50:150] = 255

ret, thresh = cv2.threshold(image,127,255,0)
print(ret.shape)

image_new,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
image = cv2.drawContours(color,contours,-1,(0,255,0),2)
cv2.imshow("image_color",color)
cv2.waitKey()
cv2.destroyAllWindows()