#Import OpenCV for image processing
#Import Time
import cv2
def videoFaceDet():

	#capture video from webcam
	video = cv2.VideoCapture('test1.mp4')

	#Cascade Classifier
	#https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html
	#The Cascade work on the principle that the classifier increasingly 
	#considers more features for the detection of faces
	#Starting off with simpler classifiers it increasingly uses them in combination 
	#for subsequent steps if the prior steps yield positive results
	#The Haar Cascade Classifier contains pre-trained classication data in XML files
	#In our case we use the Frontal Face Cascade Classifier
	#This file must be available for the purpose of classification
	
	faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

	#continuously processes video feed and displays in window until Q is pressed
	while True:
		
		#the read function gives two outputs. The check is a boolean function that returns if the video is being read
		check, frame = video.read()
		
		#Grayscale conversion of the frame
		grayImg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		
		#This is the crux of the program where discretionary parameters can be set for better results
		
		#The Scalefactor decides how many iterations the Classifier will perform in its seach for images. 
		#In every iteration, the Classifier looks for a bigger face size, starting from small and going up
		#until it is checking the entire size of the frame. The scaleFactor decides this step size. 
		#Smaller the scaleFactor, more sensitive the Classifier and longer it takes to process the frame
		
		#The minNeighbors decides the Parameter specifying how many neighbors each candidate rectangle should have to retain it.
		#Greater the minNeighbors, greater the sensitivity. However, higher might lead to false positives.
		
		#The detectMultiScale returns a list of (set of) values that can be used to build a rectangle as shown below
		faces=faceCascade.detectMultiScale(grayImg, scaleFactor=1.5, minNeighbors=5)
		print(faces)
		
		#superimposes a rectangle for all the detected images in the frame
		#(x,y) is the top left corner, (x+w, y+h) is the bottom right corner
		#(0,255,0) is colour green and 3 is the thickness of the rectangle edges
		for x, y, w, h in faces:
			frame=cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
		#window displaying the processed image
		cv2.imshow("Capturing", frame)

		#picks up the key press Q and exits when pressed
		key=cv2.waitKey(1)
		if key==ord('q'):
			break
	
	#Closes video window
	cv2.destroyAllWindows()
	
	#releases the video feed from the webcam/file
	video.release()

videoFaceDet()