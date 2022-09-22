import cv2
img=cv2.imread('puppy.jpg')
img=cv2.resize(img,(255,255))
cv2.imshow('pupppy',img)
cv2.waitKey()
cv2.destroyAllWindows()
