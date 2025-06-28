import cv2 as cv
import numpy as np

def resizwe(fa,sel=0.75):
    w=int(fa.shape[1] * sel)
    h= int(fa.shape[0] * sel)
    dimention=(w,h)
    return cv.resize(fa,dimention, interpolation=cv.INTER_AREA)

blank = np.zeros((500,500,3),dtype='uint8')
blank[:] = 64, 224, 208
resizw= resizwe(blank)
cv.imshow("dfs",blank)
cv.waitKey(0)