# -*- coding: utf-8 -*-
"""
Description: 
Plays specified video file and detects face within

Run the program like this:
$ python video1.py path/vid_file.mp4
'q' to quit

Test Vids Path:
/home/antz/0_CV3/z_samples/...
/home/antz/0_CV3/z_samples/faceVid/test5.mp4
"""
import cv2
import sys

# Get classifier
cascPath = "haarcascade_frontalface_default.xml"	# sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

# Open the video file
filename = sys.argv[1]
video_capture = cv2.VideoCapture(filename)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
