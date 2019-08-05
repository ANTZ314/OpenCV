
---------------------------
## FaceDet1:
---------------------------
#### Face Detection in still images:
[LINK](https://realpython.com/blog/python/face-recognition-with-python/)

#### Usage:

	$ python3 facedet1.py gr1.jpg
	$ python3 facedet2.py gr1.jpg
	$ python3 cam_det1.py
	$ python3 cam_det1.py
	
* facedet1.py - Opens referenced image and detects faces, then prints number faces found
* facedet2.py
	- Deep Learning Face Detector in static images using pretrained Caffe Model
	- Opens referenced image and detects faces, then prints number faces found (flags line removed)
* det_faceVid.py - Using the trained kNN network file "encodings.pickle" will make a prediction on parsed image

### MISSING??
* cam_det1.py
	* Opens default webcam and detects faces
	* Every 200 frames of captured face prints date/time
* cam_det2.py
	* Opens default webcam and detects faces
	* Every 100 frames of captured face stores image to folder

---------------------------
## FaceDet2:
---------------------------
#### More accurate Face detection with OpenCV and deep learning:
[LINK](https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/)
Taken from PyImageSearch tutorial I think?
One for detecting in images and one for videos
Prints the % accuracy of facial detection

#### Usage:

	$ python3 det_faceImg.py --image test1.jpg --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

### Change the "scaleFactor" for diff results:
-> 1.1 		- 8 correct (1 false)
-> 1.15		- 9 correct (1 false)
-> 1.2		- 7 correct (1 false)
-> 1.25 	- 7 correct (0 false)
