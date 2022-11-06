import cv2
import numpy as np

img=cv2.imread('castle.jpg')
cv2.imshow('img_org',img)


img_gray1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_gray3=cv2.cvtColor(img_gray1,cv2.COLOR_GRAY2BGR)
cv2.imshow('img_gray',img_gray3)

img_new=cv2.addWeighted(img,0.9,img_gray3,0.1,0)
cv2.imshow('img_addWeighted',img_new)
cv2.waitKey()
cv2.destroyAllWindows()

img_b,img_g,img_r=cv2.split(img)

img_r_new=cv2.addWeighted(img_r,0.1,img_gray1,0.9,0)
img_new=cv2.merge(img_b,img_g,img_r_new)
cv2.imshow('img_new',img_new)

cv2.waitKey()
cv2.destroyAllWindows()
