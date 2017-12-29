try to find contours
------

### by OpenCV
* 思路  
  先进行阈值二值化处理、利用findContours()函数提取轮廓、然后又新建一个原图的彩图（用于添加彩色轮廓线），使用drawContours()函数画出轮廓。

