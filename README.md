# OpenCV
---------

**note**: All sample images and videos moved to home folder to avoid large uploads to Github

#### 0_Mixed:
* **Bash** - 
* **coins** - 
* **contrast** - 
* **crop** - 
* **faceTest** - 
* **games** - 
* **piCam** - 
* **resize** - 
* **Notes** - 

#### 0_PyImage:
* PyImageSearch course code snippets (Chapter03 - 11)

####  anomally:
* **intro** - 
* **part1** - 
* **part2** - 

#### ballTrack:
* _UNTESTED_


#### barcode:
* **barcode**
	* Simple detection and data extraction of qr_code & barcode in static image
	* Simple detection and data extraction of qr_code & barcode in video (default camera & PiCamera options)
* **detect_barcode.py** - realtime QR code & barcode detection, draw bound and overlay interpreted string (_cv4 - ERROR_)

#### colour:  
* **Detect**
	* **detect1.py** - Opens parsed image and detects 4 colors and filters the color while overlaying the colours name
	* **detect2.py** - Opens parsed image and detects 4 colors and filters the color while overlaying the colours name (names overlap eachother)
	* **detect3.py** - same as detect1.py (code variation)
* **Games**
	* **find_games1.py** - Opens parsed image and detects 4 colors and filters the color
	* **find_games2.py** - Opens parsed image and detects 4 colors and filters the color
 
#### Digit_Rec:  
* **CreditCard**
	* **credit1** - Takes input image and crops rectangle of Card &  uses cropped image to find card details and output to console
	* **credit2** - Convert to greyscale, find contours of card. Crops the rectangular outlines of card and saves to new zoomed image
* **digitRec** - 
* **Handwriting_Database** - 
* **LiPlate_Rec** - 
* **tesseract** - 
* **vidRec** - 

#### faceCnt:  
* **single project** - Run _Face.py_ and it calls the rest (ERROR cv_V4??)

#### faceDet:  
* **FaceDet1** - 
* **FaceDet2** - 

#### faceMarks: 
* **faceMark1** - plots points of importance on human face (mouth, eyes)
* **original** - 

#### faceRec:  
* **PyImageRec** - 
* **YaleFaces** - 

#### imageScrape:  
* **google** - 
* **timecoverspider** - 

#### pedestrian:  
* **motionDet** - Displays 3 windows for tracking motion (frame, threshhold & frameDelta)
* **pedestrianDet**
	* Locates pedestrians in parsed image folder, draws bounding box and prints number of pedestrians found. 
	* Displays before and after images comparison of Non-Maxima Suppression with overlapping threshold.
* surveillance - Specifically written for Raspberry Pi - PiCamera
* **Track**
	* **detect1.py** - Opens images and detects pedestrians in each and corrects for false positives
	* **detect2.py** - Opens parsed video file detects pedestrian. Multiple false positives and EXTREMELY slow frame rate.
	* **detect3.py** - Opens default camera, finds motion & draws bounding box. Prints date/time every 50 detected frames

#### SecuriCam:  
* **motion-det** - 
* **surveillance** - 

#### social_dist:
* **social_dist.py**
	* social distancing detector. Bounding box around people, Green if okay, Red if too close to other person
	* Based on pixel distance, so must be calibrated accordingly upon setup

#### video:  
* **playback** - 
* **video** - 
* **webcam** - 
