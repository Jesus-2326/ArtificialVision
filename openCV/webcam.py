import cv2 as cv

# Read webcam
webcam = cv.VideoCapture(0)

# Visualize webcam

while True:
    ret, frame = webcam.read()
    
    cv.imshow('frame', frame)
    if cv.waitKey(40) & 0xFF==ord('q'):
        break
    
webcam.release()
cv.destroyAllWindows()