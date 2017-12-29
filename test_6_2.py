import numpy as np
import cv2

image = cv2.imread
#image = cv2.pyrDown(cv2.imread("hammer.jpg",cv2.IMREAD_UNCHANGED))
ret, thresh = cv2.threshold(cv2.cvtColor(image.copy(),cv2.COLOR_BGR2GRAY),127,255,cv2.THRESH_BINARY)
image_new, contours, hier = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:

    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int8(box)
    cv2.drawContours(image,[box],0,(0,0,255),3)

    (x,y),radius = cv2.minEnclosingCircle(c)
    center = (int(x),int(y))
    radius = int(radius)
    image = cv2.circle(image,center,radius,(0,255,0),2)

cv2.drawContours(image,contours,-1,(255,0,0),1)
cv2.imshow("contours",image)
