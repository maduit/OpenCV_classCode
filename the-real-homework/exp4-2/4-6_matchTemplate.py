from cgitb import reset
from unittest import result
import cv2 as cv
import numpy as np

def template_demo():
    src=cv.imread("./allstars.jpg")
    tpl=cv.imread("./yao.png")
    cv.imshow("imput",src)
    cv.imshow("tpl",tpl)
    th,tw=tpl.shape[:2]
    result=cv.matchTemplate(src,tpl,cv.TM_CCORR_NORMED)
    cv.imshow("result",result)
    t=0.98
    loc=np.where(result>t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(src,pt,(pt[0]+tw,th),(255,0,0),1,8,0)
    cv.imshow("matchTemplate",src)

template_demo()
cv.waitKey(0)
cv.destroyAllWindows()