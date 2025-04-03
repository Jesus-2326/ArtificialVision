import os
import cv2 as cv

# Crop

img = cv.imread(os.path.join('.','data','bird.jpg'))
img = cv.resize(img, (920,680))

cropped_img = img[80:600, 200:840] #y,x

cv.imshow('img', img)
cv.imshow('img2', cropped_img)
cv.waitKey(0)
