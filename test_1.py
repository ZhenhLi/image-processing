import numpy as np
import cv2

# 检测蓝线核圆
# OK

image = cv2.imread(r"C:\Data\project\1\PandD.tif")
cv2.imshow("image",image)
cv2.waitKey()
cv2.destroyAllWindows()

image_b = np.zeros((image.shape[0],image.shape[1]),dtype=image.dtype)
image_b[:,:] = image[:,:,2]
print(image_b.shape)
cv2.imshow("image_b",image_b)
cv2.waitKey()
cv2.destroyAllWindows()

for i in range(image_b.shape[0]):
    for j in range(image_b.shape[1]):
        if image_b[i,j] > 80:
            image_b[i,j] = 0

cv2.imshow("image_b",image_b)
cv2.waitKey()
cv2.destroyAllWindows()

image_b_canny = cv2.Canny(image_b,75,80)
cv2.imshow("image_b_canny",image_b_canny)
cv2.waitKey()
cv2.destroyAllWindows()

lines = cv2.HoughLinesP(image_b_canny,1,np.pi/180,60,minLineLength=20,maxLineGap=5)

lines1 = lines[:,0,:]
for x1,y1,x2,y2 in lines[:,0,:]:
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("lines1",image)
cv2.imwrite("blue_lines.jpg",image)
cv2.waitKey()
cv2.destroyAllWindows()

image_2 = cv2.imread(r"C:\Data\project\1\PandD.tif")
cv2.imshow("image_2",image_2)
cv2.waitKey()
cv2.destroyAllWindows()

image_2_gray = cv2.cvtColor(image_2,cv2.COLOR_RGB2GRAY)
cv2.imshow("image_2_gray",image_2_gray)
cv2.waitKey()
cv2.destroyAllWindows()

image_2_canny = cv2.Canny(image_2_gray,50,120)
cv2.imshow("image_2_canny",image_2_canny)
cv2.waitKey()
cv2.destroyAllWindows()

circles = cv2.HoughCircles(image_2_canny,cv2.HOUGH_GRADIENT,1,120
                           ,param1=100,param2=30,minRadius=35,maxRadius=80)
circles1 = circles[0,:,:]
circles1 = np.uint16(np.around(circles1))

for i in circles1[:]:
    cv2.circle(image_2,(i[0],i[1]),i[2],(255,0,0),3)
    cv2.circle(image_2,(i[0],i[1]),2,(255,0,255),3)
cv2.imshow("circles",image_2)
cv2.imwrite("circles_p1.jpg",image_2)
cv2.waitKey()
cv2.destroyAllWindows()