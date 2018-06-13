# -*- coding: utf-8 -*-
"""
Description:
Draws a green box around the red game in game1.jpg

To Run:
python find1.py game1.jpg
"""
# import the necessary packages
import numpy as np
import cv2
 
# load the games image
image = cv2.imread("game1.jpg")
#image = cv2.imread("game1.png")

## Original;
upper = np.array([65, 65, 255])
lower = np.array([0, 0, 200])

# find the red color game in the image [B G R]
#upper = np.array([50, 56, 200])
#lower = np.array([17, 15, 100])

#upper = np.array([220, 88, 50])
#lower = np.array([86, 31, 4])

#upper = np.array([62, 174, 250])
#lower = np.array([25, 146, 190])

mask = cv2.inRange(image, lower, upper)
 
# find contours in the masked image and keep the largest one
(_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,	cv2.CHAIN_APPROX_SIMPLE)
c = max(cnts, key=cv2.contourArea)
 
# approximate the contour
peri = cv2.arcLength(c, True)
approx = cv2.approxPolyDP(c, 0.05 * peri, True)
 
# draw a green bounding box surrounding the red game [B G R]
cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
cv2.imshow("Image", image)
cv2.waitKey(0)
