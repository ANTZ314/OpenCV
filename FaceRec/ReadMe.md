# PyImageRec:  

All tutorials from ** Adrian Rosebrock's ** website purely done for the purpose of learning:  
[PyImageSource](https://www.pyimagesearch.com/)

### To create a custome [Dataset](https://www.pyimagesearch.com/2018/06/11/how-to-build-a-custom-face-recognition-dataset/?__s=58mz3v4pfx9s2vjxvqgi)

Folder:	

* /home/antz/GIT31/OpenCV/FaceRec/GetFaces

**Desciption:**  
Will use opencv to find & frame instances of faces being recognised, then use keyboard to manually capture training samples of the faces you want to train with.

**To Run the Code:**  

	# Use the 'k' key to capture and the 'q' key to quit
    $ python3 build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/antz

-------------------
### PyImageSearch Face recognition [Tutorial](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)  

Folder:		

* /home/antz/GIT31/OpenCV/FaceRec/PyImRec
* /home/antz/0_samples/faceRec **(samples too big for Github)**

**Desciption:**  

* **search_bing_api.py** : Step 1 is to build a dataset (I’ve already done this for you). To learn how to use the Bing API to build a dataset with my script, just see this blog post.
* **encode_faces.py** : Encodings (128-d vectors) for faces are built with this script.  
* **recognize_faces_image.py** : Recognize faces in a single image (based on encodings from your dataset).  
* **encodings.pickle** : Facial recognitions encodings are generated from your dataset via encode_faces.py and then serialized to disk.  

No need to train a new network due to using pretrained network based on ~3 million images to construct 128-d embeddings for each image in the training set.  
The encoding stage will quantify serialise the the faces data into a file named **"encodings.pickle"**.  
Then, during classification, we can use a simple k-NN model + votes to make the final face classification.

**To Encode the Faces:**  
NOTE: Remember to set the correct training set file path:  

    $ python3 encode_faces.py --dataset /home/antz/0_samples/faceRec/dataset --encodings encodings.pickle

**To Recognise the Faces:**  
NOTE: For CPU -> set the **--detection-method** to **hog**  as the CNN face detector is slow without a GPU and RasPi doesn't have enough memory.

	$ python3 recognize_faces_image.py --encodings encodings.pickle --image /home/antz/0_samples/faceRec/examples/example_01.png
    
-------------------
### Raspberry Pi Face [Recognition](https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/)  

Folder: 

* /home/antz/GIT31/OpenCV/FaceRec/RasFaceRec
* /home/antz/0_samples/faceRec **(samples too big for Github)**

**Desciption:**  
x

**Install Dependencies:**  

    pip install dlib  
    pip install face_recognition  
    pip install imutils  

**To Run the Code:**  

	$ python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle


------------
# YaleFaces Recognition:

###  Untested fully: [link](http://hanzratech.in/2015/02/03/face-recognition-using-opencv.html)

**To Run the Code:**

	$ pytohn face_recognizer.py

======================================================
