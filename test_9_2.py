import numpy as np
import cv2

image = cv2.imread("image_canny.jpg")
cv2.imshow("image",image)
print(image.shape)
cv2.waitKey()
cv2.destroyAllWindows()

image_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("image_gray",image_gray)
cv2.waitKey()
cv2.destroyAllWindows()

image_canny = cv2.Canny(image_gray,50,100)
cv2.imshow("image_canny",image_canny)
cv2.waitKey()
cv2.destroyAllWindows()

image_1,contours,hier = cv2.findContours(image_gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

image_new = cv2.drawContours(image,contours,-1,(0,255,0),1)
cv2.imshow("image_new",image_new)
cv2.waitKey()
cv2.destroyAllWindows()

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w, y+h),(0,255,0),2)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(image,[box],0,(0,0,255),3)
    (x,y),radius = cv2.minEnclosingCircle(c)
    center = (int(x),int(y))
    radius = int(radius)
    image = cv2.circle(image,center,radius,(0,255,0),2)

cv2.drawContours(image_1, contours, -1,(255,0,0),1)


cv2.imshow("image_1",image_1)
cv2.waitKey()
cv2.destroyAllWindows()

# circles1 = cv2.HoughCircles(image_canny,cv2.HOUGH_GRADIENT,1,30,param1=10,param2=35,minRadius=20,maxRadius=50)
#
# circles = circles1[0,:,:]
# circles = np.uint16(np.around(circles))
# for i in circles[:]:
#     cv2.circle(image,(i[0],i[1]),i[2],(255,0,0),3)
#     cv2.circle(image,(i[0],i[1]),2,(255,0,255),3)
#
# cv2.imshow("image_circles",image)
# cv2.waitKey()
# cv2.destroyAllWindows()