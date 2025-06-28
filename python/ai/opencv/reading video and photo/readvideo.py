import cv2 as cv 

cap= cv.VideoCapture("semple\\videos\\face-demographics-walking-and-pause.mp4")
while True:
    isTrue, fam=cap.read()
    cv.imshow("face",fam)
    if cv.waitKey(20) & 0xff==ord('d'):
        break
#not that impotrant
fam.release()
cv.destroyAllWindows