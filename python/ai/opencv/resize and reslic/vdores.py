import cv2 as cv

vido= cv.VideoCapture("semple\\videos\\head-pose-face-detection-female.mp4")
while True:
    isTrue ,fram=vido.read()
    cv.imshow("sds",fram)
    if cv.waitKey(20) & 0xff==ord('a'):
        break
fram.release()
cv.destroyAllWindows