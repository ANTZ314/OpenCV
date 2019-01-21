# -*- coding: utf-8 -*-
"""
Description:
main

Usage:
python3 main.py
"""
import dataset as Dataset
import recog as Recog
import os

def main():
    #Here we show how to instantiate your class
    Data = Dataset.DatasetClass()           # Create object to access 'Face Capture' Class
    Face = Recog.RecogClass()				# Create object to access 'Recognition Testing' Class
    
    key = input("Capture new image: y/n - ")
    if key == 'y':
        print("Then press k to capture the image")
        Data.getPerson()                   		# allow for manual capture of person

    while(1):
    	key = input("Press: `a` to test, `q` to quit: ")

    	if key == 'a':
    		print("Find the face!!")
    		person = Face.recPerson()

    		# if no name was prominent
    		if person == "Unknown":
    			print("ACCESS DENIED MOFO!!!")
    			os.system('xdg-open dataset/dog.gif')
    		else:
    			print("YOU MAY ENTER!!!")
    			os.system('xdg-open dataset/door.mp4')

    	elif key == 'q':
    		break

    	else:
    		print("Invalid Selection Retard!!")

    print("EXITING...")
    
if __name__ == "__main__": main()