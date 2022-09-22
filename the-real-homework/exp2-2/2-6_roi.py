import cv2
import numpy as np
img = cv2.imread('puppy.jpg')
logo =cv2 .imread('logo.bmp')
cv2.imshow('img_original',img)
cv2.imshow('logo',logo)

print('size of image:{}, height:{},width:{},channel:{}'.format(img.shape,img.shape[0],img.shape[1],img.shape[2]))

#显示感兴趣的区域
cv2.imshow('img_roi',img[100:500,200:500,:])
cv2.waitKey()

#第一种图像融合方法，利用cv2.copyTo函数
h0=100
w0=200
cv2.copyTo(logo,logo,img[h0:h0+logo.shape[0],w0:w0+logo.shape[1],:])
cv2.imshow('img_logo1',img)

#第二种融合方法
h0=400
w0=600
img[h0:h0+logo.shape[0],w0:w0+logo.shape[1],:]=logo
cv2.imshow('img_logo2',img)

cv2.waitKey()
cv2.destroyAllWindows()
