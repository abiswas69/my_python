import cv2 as cv 
import time 

image=cv.imread("semple\\image\\data\\cards.png")

def resizel(frame, scal=0.75):
    width = int (frame.shape[1] *scal)
    hight = int (frame.shape[0] *scal)
    dimintion =(width,hight)
    return cv.resize(frame, dimintion, interpolation=cv.INTER_AREA)

# Resize the image
resized_image = resizel(image)  # pass the loaded image, not 'frame'

# Show the images
cv.imshow("Original", image)
cv.imshow("Resized", resized_image)
cv.waitKey(0)