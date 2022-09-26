import cv2
import numpy as np
import time
img = cv2.imread('castle.jpg')
cv2.imshow('castle',img)

t1=time.time()
img =img.astype(np.int32)
img_sharp=img.copy()
for i in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        img_sharp[i,j,:]=5*img[i,j,:]-img[i-1,j,:]- \
            img[i,j-1,:]-img[i+1,j,:]-img[i,j+1,:]
img_sharp=np.clip(img_sharp,0,255)
img_sharp=img_sharp.astype(np.uint8)
t2=time.time()

print("锐化算法1{}".format(t2-t1))
cv2.imshow('img_noised',img_sharp)
cv2.waitKey()
cv2.destroyAllWindows()