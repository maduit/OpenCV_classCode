import cv2
import numpy as np

def clamp(pv):
    if pv>255:
        return 255
    if pv<0:
        return 0
    else:
        return pv 

def gaussian_noise(image):
    h,w,c=image.shape
    for row in range(h):
        for col in range(w):
            s=np.random.normal(0,20,3)
            b=image[row,col,0]
            g=image[row,col,1]
            r=image[row,col,2]
            image[row,col,0]=clamp(b+s[0])
            image[row,col,1]=clamp(g+s[1])
            image[row,col,2]=clamp(r+s[2])
    cv2.namedWindow("npose image",cv2.WINDOW_NORMAL)
    cv2.imshow("noise image",image)
    dst=cv2.GaussianBlur(image,(5,5),0)
    cv2.namedWindow("Gaussian_Blur_image",cv2.WINDOW_NORMAL)
    cv2.imshow("Gaussian_Blur_image",dst)

src=cv2.imread("./man.jpg")
cv2.namedWindow("input_image",cv2.WINDOW_NORMAL)
cv2.imshow('input_image',src)

dst=cv2.GaussianBlur(src,(5,5),0)
cv2.namedWindow('Gaussian_Blur_src',cv2.WINDOW_NORMAL)
cv2.imshow("Gaussian_Blur_src",dst)

gaussian_noise(src)

cv2.waitKey(0)
cv2.destroyAllWindows()