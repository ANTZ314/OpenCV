"""
From:
https://www.quora.com/How-can-I-detect-an-object-from-static-image-and-crop-it-from-the-image-using-openCV

Run:
python contours.py 	(image predefined)
"""

import cv2
#reading the image 
image = cv2.imread("test.jpg")
edged = cv2.Canny(image, 10, 250)
cv2.imshow("Edges", edged)
cv2.waitKey(0)
 
#applying closing function 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed", closed)
cv2.waitKey(0)
 
#finding_contours 
(_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
	
cv2.imshow("Output", image)
cv2.waitKey(0)
