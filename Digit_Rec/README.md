
# Handwriting Recognition:

-------------------------------------------------------------------------
**A Guide to TF Layers: Building a Convolutional Neural Network:**  
https://www.tensorflow.org/tutorials/layers

-------------------------------------------------------------------------
**Yann LeCun:**  
THE MNIST DATABASE of handwritten digits:
http://yann.lecun.com/exdb/mnist/

-------------------------------------------------------------------------
**Handwritten digit database:**  
http://cis.jhu.edu/~sachin/digit/digit.html

**File format:**  
Each file has 1000 training examples. Each training example is of 
size 28x28 pixels. The pixels are stored as unsigned chars (1 byte) 
and take values from 0 to 255. The first 28x28 bytes of the file 
correspond to the first training example, 
the next 28x28 bytes correspond to the next example and so on.

Eg. In Matlab, I would use the following to read the files:
fid=fopen(data8,r);			-- open the file corresponding to digit 8
[t1,N]=fread(fid,[28 28],uchar); 	-- read in the first training example and store it in a 28x28 size matrix t1
[t2,N]=fread(fid,[28 28],uchar); 	-- read the second example into t2 and so on

To display the image use imshow(t1)

-------------------------------------------------------------------------

**Digit Recognition using OpenCV, sklearn and Python:**  
http://hanzratech.in/2015/02/24/handwritten-digit-recognition-using-opencv-sklearn-and-python.html


