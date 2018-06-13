# -*- coding: utf-8 -*-
"""
Description:
Opens default webcam and detects faces

Run the program like this:
$ python webcam.py
"""
import cv2
import sys

# Get classifier
cascPath = "haarcascade_frontalface_default.xml"	# sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

# Capture from Camera
video_capture = cv2.VideoCapture(0)

def main():
	while True:
		# Capture frame-by-frame
		ret, frame = video_capture.read()#FFFFFF

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
	print("Exit!!")

if __name__ == "__main__": main()
