import cv2
import numpy as np

img=cv2.imread('castle.jpg')
cv2.imshow('img_org',img)

img_hsv=img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('img_hsv',img_hsv)

img_h,img_s,img_v=cv2.split(img_hsv)

img_v=cv2.add(img_v,50)

img_hsv_new=cv2.merge((img_h,img_s,img_v))
cv2.imshow('img_hsv_new',img_hsv_new)

img_new=cv2.cvtColor(img_hsv_new,cv2.COLOR_HSV2BGR)
cv2.imshow('img_new',img_new)

cv2.waitKey()
cv2.destroyAllWindows()