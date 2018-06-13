
Webcam-Face-Detect
==================
Description:
------------
webcam1a.py	- Opens default webcam and detects faces

webcam1b.py	- Same, except "detectMultiScale" is simplified

webcam1c.py	- Adapted to Raspberry Pi using picamera

webcam2a.py	- Default camera, detects faces [Version1]
		- Every 200 faces detected, increments counter / trigger
		
webcam2b.py	- Default camera, detects faces [Version1]
		- Every 200 faces detected, saves image capture as "date time.png"

webcam3.py	- Default camera, detects faces [Version2]

webcam4.py	- Detects motion and frames it (person finder)

-----------------------------------------------------------------
alpython.com/blog/python/face-detection-in-python-using-a-webcam/
Update: Now supports OpenCV3. This change has been made by furetosan ( https://github.com/furetosan) and tested on Linux.
To run the OpenCV3 version, run python webcam_cv3.py haarcascade_frontalface_default.xml

