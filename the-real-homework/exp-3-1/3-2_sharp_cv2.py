import cv2
import numpy as np
import time
img = cv2.imread('castle.jpg')
cv2.imshow('castle',img)

t1=time.time()
kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
print(kernel)
img_noised=cv2.filter2D(img,-1,kernel)

t2=time.time()
print('算法3花费的时间为{}'.format(t2-t1))
cv2.imshow('img_noised',img_noised)
cv2.waitKey()
cv2.destroyAllWindows()