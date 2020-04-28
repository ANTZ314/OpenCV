"""
* From:
* http://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/

* Description:
* Finds and displays colour presence in the image Red, Blue, Yellow, Grey [game2.jpg]
* game3.jpg doesn't find the yellow pin??
*
* USAGE:
* python find2.py --image game2.png
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

# define the list of boundaries
boundaries = [
	([17, 15, 100], [50, 56, 200]),			# R
	([86, 31, 4], [220, 88, 50]),			# B
	([25, 146, 190], [62, 174, 250]),		# Y
	([103, 86, 65], [145, 133, 128])		# Grey
]

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
