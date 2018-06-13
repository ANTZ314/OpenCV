# -*- coding: utf-8 -*-
"""
Description:
Draws a green box around the red game in game1.jpg

To Run:
python crop2.py --image card0.png

If full path needed:
python crop2.py --image /home/antz/0_CV3/z-Test/crop/crop4/card0.png
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
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	edged = cv2.Canny(image, 10, 250)
	(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	c = max(cnts, key=cv2.contourArea)
	idx = 0
	
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	
	x,y,w,h = cv2.boundingRect(approx) #
	new_img=image[y:y+h,x:x+w] #
	cv2.imwrite(str(idx) + '.png', new_img) #
		
	cv2.imshow("im",image)
	cv2.waitKey(0)

if __name__ == '__main__': main()
