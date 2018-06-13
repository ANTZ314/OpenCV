# -*- coding: utf-8 -*-
"""
Description:
Draws a green box around the red game in game1.jpg

To Run:
python crop1.py --image card0.png

If full path needed:
python crop1.py --image /home/antz/0_CV3/z-Test/crop/crop4/card0.png
"""
import cv2
import argparse

def main():
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", help = "path to the image")
	args = vars(ap.parse_args())

	# load the image & pre-process
	image = cv2.imread(args["image"])
	edged = cv2.Canny(image, 10, 250)
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
	closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

	#finding_contours 
	(_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	c = max(cnts, key=cv2.contourArea)

	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)

	cv2.imshow("Output", image)
	cv2.waitKey(0)

if __name__ == '__main__': main()
