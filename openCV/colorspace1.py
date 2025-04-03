import os 
import cv2 as cv

img = cv.imread(os.path.join('.','data','bird.jpg'))

img = cv.resize(img, (920,680))
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow('img', img)
cv.imshow('imgRGB', img_rgb)
cv.imshow('imgGRAY', img_gray)
cv.imshow('imghsv', img_hsv)
cv.waitKey(0)