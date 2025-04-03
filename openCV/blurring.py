import os
import cv2 as cv

img = cv.imread(os.path.join('.','data','bird.jpg'))
img = cv.resize(img, (920,680))

k_size = 15
img_blur = cv.blur(img, (k_size,k_size))
img_gaussina_blur = cv.GaussianBlur(img, (k_size,k_size),3)
img_median_blur = cv.medianBlur(img, k_size) #Para ruido

cv.imshow('img', img)
cv.imshow('img2', img_blur)
cv.imshow('img3', img_gaussina_blur)
cv.imshow('img4', img_median_blur)
cv.waitKey(0)