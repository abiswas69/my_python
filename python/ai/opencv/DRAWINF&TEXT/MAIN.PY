import cv2 as cv 

def resizwe(fa,sel=0.75):
    w=int(fa.shape[1] * sel)
    h= int(fa.shape[0] * sel)
    dimention=(w,h)
    return cv.resize(fa,dimention, interpolation=cv.INTER_AREA)


img= cv.imread('semple\\image\\team1.jpg')
resizw= resizwe(img)
show=cv.imshow("draw",resizw)
cv.waitKey(0)
cv.destroyAllWindows()
