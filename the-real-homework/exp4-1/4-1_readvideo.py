# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:40:17 2022

@author: Administrator
"""

import cv2
import sys


cap=cv2.VideoCapture('bike.avi')

if not cap.isOpened():
    print('打开错误')
    sys.exit()

fps=int(cap.get(cv2.CAP_PROP_FPS))
l=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('帧率为{}，帧数为{}，尺寸为{}'.format(fps,l,size))

while True:
    rect,frame=cap.read()
    
    if frame is None:
        break
    cv2.imshow('bike',frame)
    key=cv2.waitKey(100)
    if key ==27:
        break
    if key==ord("s"):
        cv2.imwrite('img.bmp',frame)

cv2.destroyAllWindows()
cap.release()