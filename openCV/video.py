import os
import cv2 as cv

# Read Video
video_path = os.path.join('.','data','money.mp4')
video = cv.VideoCapture(video_path)

#Visualize video