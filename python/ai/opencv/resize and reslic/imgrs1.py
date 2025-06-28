import cv2 as cv

#i find two to resize image frist 

image=cv.imread("semple\\image\\data\\cards.png")
resoze=cv.resize(image,(500,300))
see=cv.imshow("name",resoze)
cv.waitKey(0)
cv.destroyAllWindows
"""
this code i leran from wscube tech youtube 
and anytgor one is 
"""