import numpy as np
import cv2

# Ptoject 8
# OK

# 请从图像中分割出珍珠，并检测出边缘

image = cv2.imread(r"C:\Data\project\8\pearls.jpg")
cv2.imshow("image",image)
print(image.shape)
cv2.waitKey()
cv2.destroyAllWindows()

kernel_3x3 = np.array([[-1,-1,-1],
                       [-1,8,-1],
                       [-1,-1,-1]])

b = np.array(kernel_3x3)
print(b.flatten())

kernel_5x5 = np.ones((5,5),np.uint8)

image_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("image_gray",image_gray)
cv2.waitKey()
cv2.destroyAllWindows()

image_blur = cv2.GaussianBlur(image_gray, (11,11),0)
cv2.imshow("image_blur",image_blur)
cv2.waitKey()
cv2.destroyAllWindows()

g_hpf = image_gray - image_blur
cv2.imshow("g_hpf",g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()

image_dilate = cv2.dilate(g_hpf,kernel_3x3,iterations=1)
cv2.imshow("image_dilate",image_dilate)
cv2.waitKey()
cv2.destroyAllWindows()

image_canny = cv2.Canny(image_dilate,100,180)
cv2.imshow("image_canny",image_canny)
cv2.waitKey()
cv2.destroyAllWindows()

circles = cv2.HoughCircles(image_canny,cv2.HOUGH_GRADIENT,1,30
                           ,param1=10,param2=35,minRadius=20,
                           maxRadius=50)
circles1 = circles[0,:,:]
circles = np.uint16(np.around(circles1))

for i in circles1[:]:
    cv2.circle(image,(i[0],i[1]),i[2],(255,0,0),3)
    cv2.circle(image,(i[0],i[1]),2,(255,0,255),3)

cv2.imshow("image_circles",image)
cv2.waitKey()
cv2.destroyAllWindows()