import numpy as np
import cv2

img=cv2.imread('sig1.jpg',0)
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
img=cv2.resize(thresh,(960,540))
cv2.imshow('image',img)

if cv2.waitKey(1)==27:
   cv2.destroyAllWindows()
