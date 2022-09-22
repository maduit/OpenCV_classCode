import cv2
src=cv2.imread('puppy.jpg')#读取
cv2.imshow('puppy',src)#显示正常图片
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)#转换为灰度图
# cv2.namedWindow("input",cv2.WINDOW_AUTOSIZE)
# namedWindow()        于创建显示图像的窗口
# cv2.WINDOW_AUTOSIZE	不可调窗口大小
# cv2.WINDOW_NORMAL		可调整窗口大小
cv2.imshow("gray",gray)#显示灰度图
cv2.waitKey(0)
cv2.destroyAllWindows()