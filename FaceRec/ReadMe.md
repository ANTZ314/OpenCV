# PyImageRec:

### To Gather the [Dataset](https://www.pyimagesearch.com/2018/06/11/how-to-build-a-custom-face-recognition-dataset/?__s=58mz3v4pfx9s2vjxvqgi)

Folder:	

* /home/antz/GIT31/OpenCV/FaceRec/GetFaces

**Desciption:**  
Will use opencv to find & frame instances of faces being recognised, then use keyboard to manually capture training samples of the faces you want to train with.

**To Run the Code:**  

	# Use the 'k' key to capture and the 'q' key to quit
    $ python3 build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/antz

-------------------
### PyImageSearch Face recognition [Tutorial](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)  

Path:		

* /home/antz/GIT31/OpenCV/FaceRec/PyImRec
* /home/antz/0_samples/faceRec **(samples too big for Github)**

**Dependencies**
* face_recognition
* dlib

**Desciption:**  

* **encode_faces.py** : Encodings (128-d vectors) for faces are built with this script. Point to training set (min 5 images?)  
* **faceRecImage.py** : Recognize faces in a single image (based on encodings from your dataset).  
**faceRecVideo.py** : Recognise faces based on the pre-trained **encode_faces.pickle** file in parsed video file.  
* **encodings.pickle** : Facial recognitions encodings are generated from your dataset via encode_faces.py and then serialized to disk.  

####Note:

No need to train a new network due to using pretrained network based on ~3 million images to construct 128-d embeddings for each image in the training set.  
The encoding stage will quantify serialise the the faces data into a file named **"encodings.pickle"**.  
Then, during classification, we can use a simple k-NN model + votes to make the final face classification.

**To Encode the Faces:**  
NOTE: Remember to set the correct training set file path:  

    $ python3 encode_faces.py --dataset /home/antz/0_samples/faceRec/dataset --encodings encodings.pickle

**To Recognise the Faces:**  
NOTE: For CPU -> set the **--detection-method** to **hog**  as the CNN face detector is slow without a GPU and RasPi doesn't have enough memory.

	$ python faceRecImage.py --encodings encodings.pickle --image /home/antz/0_samples/faceRec/examples/ex0.png
	
	$ python faceRecVideo.py --encodings encodings.pickle --output /home/antz/0_samples/faceRec/output/faceRec.avi --display 0

-------------------
#### faceReact

**Path:**

* /home/antz/GIT31/OpenCV/FaceRec/faceReact

**Description:** 

**main.py** - Main Class calling 2 other classes: dataset.py & recog.py. Also recieves the classification and determines the reaction.
* **dataset.py** - Determine an instance of facial detection to Capture an clean facial image from default camera. 
* **recog.py** - Using the previously generated "encodings.pickle" file, it performs a classification of the capture face. If there is a match, a video is played. If there is no match a specified gif is played.

 **To Run the Code:**  
 
 	$ python3 main.py
    
-------------------
#### Raspberry Pi Face [Recognition](https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/)  

Path: 

* /home/antz/GIT31/OpenCV/FaceRec/RasFaceRec
* /home/antz/0_samples/faceRec **(samples too big for Github)**

**Dependencies:**
* face_recognition
* dlib
* pickle
* cv2

**Desciption:**  

* **Original** - Directly from tutorial where classifier is optimised for the RasPi and will recognise in camera video stream.

* **rasFaceRec**  

	* My adapted version from faceReact, using single image capture for recognition and then react to classification. 
* Changed cnn to **hog** due to processing power and available memory.
* Replaced **subprocess** with **xdg-open** to play reactionary videos.
* Hopefully replace video reaction with **LOCK** or **UNLOCK**

**To Run the Code:**  

	$ python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle


------------
# YaleFaces:

###  [link](http://hanzratech.in/2015/02/03/face-recognition-using-opencv.html)

**To Run the Code:**

	$ pytohn face_recognizer.py
