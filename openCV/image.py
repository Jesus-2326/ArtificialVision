import os
import cv2 as cv

# Read image 
image_path = os.path.join('.', 'data', 'bird.jpg')
img = cv.imread(image_path)

# Write image
cv.imwrite(os.path.join('.', 'data', 'bird_out.jpg'), img)

# visualize image
cv.imshow('Image', img)
cv.waitKey(0)