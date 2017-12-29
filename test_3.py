import numpy as np
import cv2

# Project 3 检测瓶子高度
# OK

# 读入图像
image = cv2.imread(r"C:\Data\project\3\1.jpg")
print(image.shape)  # 显示图像形状
cv2.imshow("image",image)   # 输出图像
cv2.waitKey()
cv2.destroyAllWindows()
# 转灰度图像
image_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("image_gray",image_gray)
print(image_gray.shape)
cv2.waitKey()
cv2.destroyAllWindows()
# 固定阈值二值化（此处还可尝试其他二值化方法）
retval, image_fixed_bina = cv2.threshold(image_gray,200,255,cv2.THRESH_BINARY)
# 前者为边缘，后者为得到的二值化图像
cv2.imshow("image_fixed_bina",image_fixed_bina)
cv2.waitKey()
cv2.destroyAllWindows()
# 腐蚀图像
kernel = np.ones((5,5),np.uint8)
kernel_5x5 = np.array([[0,0,1,0,0],
                       [0,0,1,0,0],
                       [1,1,1,1,1],
                       [0,0,1,0,0],
                       [0,0,1,0,0]])

image_erosion = cv2.erode(image_fixed_bina,kernel_5x5,iterations=1)
cv2.imshow("image_erosion",image_erosion)
print(image_erosion.shape)
cv2.waitKey()
cv2.destroyAllWindows()

# 任务结束

# 附加说明：

# 腐蚀应用场合：

# 边缘检测
# 噪声滤除
# 形态骨架提取

# 消除噪声
# 分割出独立的图像元素，在图像中连接相邻元素
# 寻找图像中明显的极大值极小值区域
# 求出图像的梯度

# 腐蚀：删除对象边界某些像素
# 求局部最小值
# 腐蚀一般用来消除噪点，分割独立的图像元素
# 腐蚀操作一般对二值化进行处理：中心元素是否与周围领域像素点颜色一样，若为白色点，则值是否为255，是则保留，否则该点变为黑色（0）
# 上面腐蚀图像中的 kernel \ kernel_5x5 都为模板，默认空

# 腐蚀过程：拿B的中心点与X上的点一个一个地比对，如果B上所有点在X的范围内，则该点保留，否则该点要去掉（变为白点），
#          可以看出，它仍在原来X的范围内，且比X包含的点要少，就像X被腐蚀掉了一层。

# 数学角度理解腐蚀和膨胀：
# 将图像与核进行卷积，核可以是任何的形状和大小，它拥有一个单独定义出来的参考点：锚点，
# 多数情况下，核是一个小的中间带有参考点核实心正方形或者圆盘

# 关于膨胀：
# 腐蚀的反操作
# 使图像中高亮区域逐渐增长
# 相当于求局部最大值

# 结构元素：图像X,B，X为待处理对象，B是用来处理X的，则称B为结构元素，即刷子，结构元素一般为一些比较小的图像。

