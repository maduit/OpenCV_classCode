import cv2
import numpy as np

img =cv2.imread('castle.jpg')
cv2.imshow('img_org',img)

h,w,c=img.shape[0],img.shape[1],img.shape[2]
print("img的尺寸为{}，高为{}，宽为{}，通道数为{}".format(img.shape,h,w,c))

img_noise=np.zeros(img.shape,dtype=np.uint8)

thred=0.1
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        ratio =np.random.rand()
        #   print(ratio)
        if ratio<thred:
            img_noise[i,j]=255
        else:
            img_noise[i,j]=img[i,j]
cv2.imshow('img_noise',img_noise)

cv2.waitKey()
cv2.destroyAllWindows()