import cv2
import numpy as np

img1=cv2.imread('castle.jpg')
img1=cv2.resize(img1,(200,200))
cv2.imshow('castle',img1)
cv2.waitKey()

img2=cv2.imread('rain.jpg')
img2=cv2.resize(img2,(200,200))
cv2.waitKey()

img3=cv2.add(img1,img2)
cv2.imshow('rain castle1',img3)


img4=cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('rain castle2',img4)
cv2.waitKey()

img5=cv2.add(img1,50)
cv2.imshow('dark castle',img5)
cv2.waitKey()
cv2.destroyAllWindows()