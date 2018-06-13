"""
From:
https://stackoverflow.com/questions/28773186/what-does-ret-and-frame-mean-here

Description:
Simple example of using cv2 to playback video source frame-by-frame with
'waitkey(x)' value determining the playback frame-rate
'out' determines the window size and ?? (60.0?)

Use:
python simplePlay2.py --video /home/antz/0_CV3/FaceVid/playback/output.avi
'q' to quit
"""
import argparse
import numpy as np
import cv2

#cap = cv2.VideoCapture('/home/antz/0_CV3/FaceVid/0vids/29secOut.mp4')

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
args = vars(ap.parse_args())

# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
	cap = cv2.VideoCapture(0)
	time.sleep(0.25)
# otherwise, we are reading from a video file
else:
	cap = cv2.VideoCapture(args["video"])
	
# Define the codec and create VideoWriter object
# fourcc = cv2.cv.CV_FOURCC(*'MJPG')
out = cv2.VideoWriter('output.mpg',0, 60.0, (640,480))

while(cap.isOpened()):
	# Capture frame-by-frame
	ret, frame = cap.read()
	
	if ret==True:
		# flip the video output
		#frame = cv2.flip(frame,0)
		
		# write the flipped frame and show
		out.write(frame)
		cv2.imshow('video window',frame)
		
		# 'q' to exit & wait value determines playback speed (fps)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
