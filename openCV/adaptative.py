import os
import cv2 as cv

# Crop

img = cv.imread(os.path.join('.','data','carta.jpg'))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

thresh = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,21,30)

cv.imshow('img', img)
cv.imshow('img2', thresh)


cv.waitKey(0)
