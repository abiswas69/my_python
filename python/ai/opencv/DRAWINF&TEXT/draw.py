import cv2 as cv
import numpy as np

blank = np.zeros((500,500),dtype='uint8')
cv.imshow("dfs",blank)
cv.waitKey(0)