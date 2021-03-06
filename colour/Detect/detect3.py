# -*- coding: utf-8 -*-
"""
* From:
* http://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
* 
* Description:
*
* USAGE:
* python detect3.py --image games.png
* python detect3.py --image tacks.jpg			<--- image needs to be resized smaller

Note: If error try full file path to the image
"""
# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries (Red/Blue/Yellow/Grey)
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

def main():
	# loop over the boundaries
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")

		# find the colors within the specified boundaries and apply the mask
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)

		# show the images
		cv2.imshow("images", np.hstack([image, output]))
		cv2.waitKey(0)

if __name__ == "__main__": main()
