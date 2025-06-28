import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# Draw a circle at the center
center = (blank.shape[1]//2, blank.shape[0]//2)
cv.circle(blank, center, 40, color=(64, 224, 208), thickness=7)

# Draw a line from the center to some point (here I'm drawing a horizontal line to the right)
end_point = (blank.shape[1]//2 + 100, blank.shape[0]//2)  # 100 pixels to the right
cv.line(blank, center, end_point, color=(64, 224, 208), thickness=1)

cv.imshow("Drawing", blank)
cv.waitKey(0)
cv.destroyAllWindows()