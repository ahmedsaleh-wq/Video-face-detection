import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
def resize_video(frame, scale=0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

video = cv.VideoCapture('video-1.mp4')

while True:
    isTrue, frame = video.read()
    resize = resize_video(frame)
    gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    for (x, y, w, h) in faces_rect:
        cv.rectangle(resize, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv.imshow('video', resize)

    if cv.waitKey(20) & 0XFF==ord('d'):
        break
video.release()
cv.destroyAllWindows()