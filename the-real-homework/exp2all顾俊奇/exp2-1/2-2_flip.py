import cv2
img =cv2.imread(".//puppy.jpg")
img = cv2.resize(img,(256,150))
cv2.imshow('puppy',img)#显示图像

img_flip_v=cv2.flip(img,0)#垂直翻转
cv2.imshow("puppy_flip_V",img_flip_v)#显示图像

img_flip_h=cv2.flip(img,1)#水平翻转
cv2.imshow('puppy_flip_h',img_flip_h)#显示图像

cv2.waitKey()#键盘响应，去掉，不显示
cv2.destroyAllWindows()#销毁窗口