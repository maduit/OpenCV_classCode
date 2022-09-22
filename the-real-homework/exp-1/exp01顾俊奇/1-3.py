import glob as gb #导入glob模块
import cv2
# 返回该路径下所有的 jpg 文件的路径
img_path = gb.glob("E:\homework\exp-1\images/*.png")
img_path2 = gb.glob("E:\homework\exp-1\images/*.jpg")
i="0"
for path in img_path:
    img = cv2.imread(path)
    cv2.imshow("3066"+"+"+i, img)
    cv2.imwrite("3066"+"+"+i+'.png',img)
    i=str(int(i)+1)
    cv2.waitKey()   
    cv2.destroyAllWindows()
for path in img_path2:
    img = cv2.imread(path)
    cv2.imshow("3066"+"+"+i, img)
    cv2.imwrite("3066"+"+"+i+'.jpg',img)
    i=str(int(i)+1)
    cv2.waitKey()   
    cv2.destroyAllWindows()