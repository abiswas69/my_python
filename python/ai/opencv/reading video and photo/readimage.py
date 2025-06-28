import cv2  # Correct import statement for OpenCV

image = cv2.imread("semple\\image\\hand.jpg")  # Using OpenCV functions via cv2
cv2.imshow("Image", image)
cv2.waitKey(0)