import cv2 as cv
import numpy as np
"""this function not that improten
if you want thant don't use it """
def resizwe(fa,sel=0.75):
    w=int(fa.shape[1] * sel)
    h= int(fa.shape[0] * sel)
    dimention=(w,h)
    return cv.resize(fa,dimention, interpolation=cv.INTER_AREA)

blank = np.zeros((500,500,3),dtype='uint8')


cv.rectangle(blank,(235,450),(5000,2200),(64, 224, 208),thickness=3, lineType=1 ,shift=4)


#     this is to fill all                                 thickness=cv.FILLED
# cv.rectangle(blank,(235,450),(5000,2200),(64, 224, 208),thickness=cv.FILLED, lineType=1 ,shift=4)

resizw= resizwe(blank)
cv.imshow("dfs",blank)
cv.waitKey(0)
cv.destroyAllWindows()