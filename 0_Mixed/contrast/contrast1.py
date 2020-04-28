# -*- coding: utf-8 -*-
"""
Description:
Increase brightness/contrast of image

To Run:
python find1.py game1.jpg
"""
# import the necessary packages
import cv2

#img = cv2.imread('test.jpg')
img = cv2.imread('lena_low.gif')
cv2.imshow('test', img)
cv2.waitKey(1000)
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


imghsv[:,:,2] = [[max(pixel - 25, 0) if pixel < 190 else min(pixel + 25, 255) for pixel in row] for row in imghsv[:,:,2]]
cv2.imshow('contrast', cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR))
cv2.waitKey(1000)
#raw_input()

if cv2.waitKey(1):
	cv2.destroyAllWindows()
	print("Destroy & Exit!!")
