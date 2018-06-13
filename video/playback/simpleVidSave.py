# -*- coding: utf-8 -*-
"""
Playback video file:
http://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html
"""





import numpy as np
import cv2

# Use the defauolt camera as video source
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
 
while(cap.isOpened()):
	# Capture frame-by-frame
	ret, frame = cap.read()
	
	if ret==True:
		# flip the video output
		#frame = cv2.flip(frame,0)
		
		# write the flipped frame and show
		out.write(frame)
		cv2.imshow('frame',frame)
		
		# 'q' to exit & wait value determines playback speed (fps)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break
		
# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
