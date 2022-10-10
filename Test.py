from email.mime import image
from string import hexdigits
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    blur_frame = cv.GaussianBlur(frame,(9,9),0)
    cv.imshow("Live Cam", blur_frame)
    if cv.waitKey(1) == 13:
        break

#def init():
cap.release()

cv.destroyAllWindows