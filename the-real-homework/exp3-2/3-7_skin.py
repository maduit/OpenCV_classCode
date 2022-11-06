import cv2
import numpy as np
import time


img=cv2.imread('girl.jpg')
cv2.imshow('img',img)

img_YCrCb=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
cv2.imshow('img_YCrCb',img_YCrCb)

img_skin_model=np.zeros((256,256,1),dtype=np.uint8)



cv2.ellipse(img_skin_model,(113,155),(23,15),43,0,360,255,-1)
cv2.imshow('img_skin_model',img_skin_model)

t1=time.time()
mask=img_skin_model[img_YCrCb[:,:,1],img_YCrCb[:,:,2]]
skin1=cv2.copyTo(img,mask)
t2=time.time()
cv2.imshow('skin1',skin1)
cv2.imshow('mask',mask)

t3=time.time()
skin2=np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        cr=img_YCrCb[i,j,1]
        cb=img_YCrCb[i,j,2]
        if img_skin_model[cr,cb]>0.5:
            skin2[i,j]=img[i,j]
        else:
            skin2[i,j]=0
t4=time.time()
print('算法1所用时间：{}s，算法2所用时间：{}s'.format(t2-t1,t4-t3))
cv2.imshow('skin2',skin2)
cv2.waitKey()
cv2.destroyAllWindows()
 
    
