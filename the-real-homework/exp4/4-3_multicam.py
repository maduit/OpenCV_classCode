# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
img=cv2.imread("puppy.jpg")
img=cv2.resize(img,(320,240))
while True:
    rect,frame=cap.read()
    if rect:
        frames=np.hstack([frame,frame])
        frames2=np.vstack([frames,frames])
        cv2.imshow("video",frames)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()