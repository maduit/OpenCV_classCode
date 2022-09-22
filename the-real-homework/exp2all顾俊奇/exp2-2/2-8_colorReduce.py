from gettext import npgettext
import cv2
import numpy as np

img =cv2.imread('castle.jpg')
cv2.imshow('img_org',img)

interval=64
tmp=interval/2+np.zeros(img.shape)
tmp=tmp.astype(np.uint8)
cv2.imshow('tmp',tmp)
img_reduce=cv2.add((img/interval).astype(np.uint8)*interval,tmp)

cv2.imshow('img_reduce',img_reduce)
cv2.waitKey()
cv2.destroyAllWindows()