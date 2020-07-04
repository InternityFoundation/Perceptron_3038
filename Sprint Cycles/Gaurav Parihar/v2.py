#Import OpenCV for image processing
#Import Time
import cv2
def videoFaceDet():

	#capture video
	video = cv2.VideoCapture('test1.mp4')

	#Cascade Classifier
	
	faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

	#continuously processes video feed and displays in window until Q is pressed
	while True:
		
		#the read function gives two outputs. The check is a boolean function that returns if the video is being read
		check, frame = video.read()
		
		#Grayscale conversion of the frame
		grayImg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		
		faces=faceCascade.detectMultiScale(grayImg, scaleFactor=1.5, minNeighbors=5)
		print(faces)
		
		#superimposes a rectangle for all the detected images in the frame
		#(x,y) is the top left corner, (x+w, y+h) is the bottom right corner
		#(0,255,0) is colour green and 3 is the thickness of the rectangle edges
		for x, y, w, h in faces:
			frame=cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
		#window displaying the processed image
		cv2.imshow("Capturing", frame)
		key=cv2.waitKey(1)
		if key==ord('q'):
			break
	
	#Closes video window
	cv2.destroyAllWindows()
	
	#releases the video feed from the webcam/file
	video.release()

videoFaceDet()