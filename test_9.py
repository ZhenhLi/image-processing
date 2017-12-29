import numpy as np
import cv2

# Project 9
# 分割珍珠并检测其边缘

image = cv2.imread(r"C:\Data\project\9\pearls2.jpg")
cv2.imshow("image",image)
cv2.waitKey()
cv2.destroyAllWindows()
#image_2 = image.copy()
image_2,contours_2,hierarchy_2 = cv2.findContours(image[:,:,0],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image_n_2 = cv2.drawContours(image,contours_2,-1,(0,255,0),2)
cv2.imshow("contours",image_n_2)
cv2.waitKey()
cv2.destroyAllWindows()

# rgb转hsi
# 方法一：
image_hsi = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
cv2.imshow("image_hsi",image_hsi)
#cv2.waitKey()
#cv2.destroyAllWindows()
# 方法二：
def rgb2hsi(rgb_image):
    rows = int(rgb_image.shape[0])
    cols = int(rgb_image.shape[1])
    b,g,r = cv2.split(rgb_image)

    b = b/255.0
    g = g/255.0
    r = r/255.0
    hsi_image = rgb_image.copy()
    H, S, I = cv2.split(hsi_image)
    for i in range(rows):
        for j in range(cols):
            num = 0.5 * ((r[i,j]-g[i,j])+(r[i,j]-b[i,j]))
            den = np.sqrt((r[i,j]-g[i,j])**2 + (r[i,j]-b[i,j])*(g[i,j]-b[i,j]))
            theta = float(np.arccos(num/den))

            if den == 0:
                H = 0
            elif b[i,j] <= g[i,j]:
                H = theta
            else:
                H = 2 * 3.14159265 - theta
            min_RGB = min(min(b[i,j],g[i,j]),r[i,j])
            sum = b[i,j] + g[i,j] + r[i,j]
            if sum ==0:
                S = 0
            else:
                S = 1 - 3 * min_RGB/sum # 除去sum时感觉边界轮廓更好一些，不失为一个方法

            H = H/(2*3.14159265)
            I = sum/3.0

            hsi_image[i,j,0] = H*255
            hsi_image[i,j,1] = S*255
            hsi_image[i,j,2] = I*255
    return hsi_image

image_hsi_2 = rgb2hsi(image)
cv2.imshow("image_hsi_1",image_hsi_2)
cv2.waitKey()
cv2.destroyAllWindows()

h_1,s_1,i_1 = cv2.split(image_hsi_2)
cv2.imshow("h_1",h_1)
cv2.imshow("s_1",s_1)
cv2.imshow("i_1",i_1)
cv2.waitKey()
cv2.destroyAllWindows()
# 叠加 H 和 S 空间
add_hs = image_hsi_2[:,:,0] + image_hsi_2[:,:,1]
cv2.imshow("add_hs",add_hs)
print(add_hs.shape)
print(add_hs[1,1])
cv2.waitKey()
cv2.destroyAllWindows()

b2w = image.copy()
for i in range(add_hs.shape[0]):
    for j in range(add_hs.shape[1]):
        if add_hs[i,j] < 255*0.6:
            b2w[i,j] = 255
        elif add_hs[i,j] > 255*0.9:
            b2w[i,j] = 255
        else:
            b2w[i,j] = 0

cv2.imshow("b2w",b2w)
cv2.waitKey()
cv2.destroyAllWindows()

image_new,contours,hierarchy = cv2.findContours(add_hs, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("image_new",image_new)
image_new2 = cv2.drawContours(b2w,contours,-1,(0,255,0),1)
cv2.imshow("image_new2",image_new2)
cv2.waitKey()
cv2.destroyAllWindows()

kernel_3x3 = np.array([[-1,-1,-1],
                       [-1,8,-1],
                       [-1,-1,-1]])

image_dilate = cv2.dilate(b2w,kernel_3x3,iterations=1)
image_erode = cv2.erode(image_dilate,kernel_3x3,iterations=1)
cv2.imshow("image_dilate",image_dilate)
cv2.imshow("image_erode",image_erode)
cv2.waitKey()
cv2.destroyAllWindows()

image_canny = cv2.Canny(image_erode,50,80)
cv2.imshow("image_canny",image_canny)
cv2.imwrite("image_canny.jpg",image_erode)
cv2.waitKey()
cv2.destroyAllWindows()



#cv2.HoughCircles()
# circles1 = cv2.HoughCircles(image_canny,cv2.HOUGH_GRADIENT,1,120,param1=10,param2=35,minRadius=20,maxRadius=50)
# #print(circles[0,1,1])
# circles = circles1[0,:,:]
# circles = np.uint16(np.around(circles))
#
# for i in circles[:]:
#     cv2.circle(image,(i[0],i[1]),i[2],(255,0,0),3)
#     cv2.circle(image,(i[0],i[1]),2,(255,0,255),3)
#
# cv2.imshow("image_circles",image)
# cv2.waitKey()
# cv2.destroyAllWindows()