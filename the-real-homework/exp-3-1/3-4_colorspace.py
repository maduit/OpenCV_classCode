import cv2
import numpy as np
flags=[i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

img =cv2.imread('castle.jpg')
cv2.imshow('img_org',img)

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray',img_gray)

img_LAB=cv2.cvtColor(img,cv2.COLOR_BGR2Lab)
cv2.imshow('img_LAB',img_LAB)

img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('img_hsv',img_hsv)

img_YCrCb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
cv2.imshow('img_YCrCb',img_YCrCb)

cv2.waitKey()
cv2.destroyAllWindows()