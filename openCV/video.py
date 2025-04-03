import os
import cv2 as cv

# Read Video
video_path = os.path.join('.','data','1.mp4')
video = cv.VideoCapture(video_path)

#Visualize video
ret = True
while ret:
    ret, frame = video.read()
    
    if ret:
        cv.imshow('frame', frame)
        cv.waitKey(60)
        
video.release()
cv.destroyAllWindows()