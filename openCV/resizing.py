import os
import cv2 as cv

img = cv.imread(os.path.join('.','data','bird.jpg'))

resized_img = cv.resize(img, (640,480))


#print(img.shape)

cv.imshow('img', img)
cv.imshow('img2', resized_img)
cv.waitKey(0)