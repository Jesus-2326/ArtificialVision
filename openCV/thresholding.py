import os
import cv2 as cv

# Crop

img = cv.imread(os.path.join('.','data','bird.jpg'))
img = cv.resize(img, (920,680))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray,80,255, cv.THRESH_BINARY)

thresh = cv.blur(thresh, (10,10))
ret, thresh = cv.threshold(img_gray,80,255, cv.THRESH_BINARY)

cv.imshow('img', img_gray)
cv.imshow('thresh', thresh)

cv.waitKey(0)
