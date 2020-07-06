#Import OpenCV for image processing
#Import Time
import os
import cv2
import numpy as np
import faceRecognition as fr
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData2.yml')

name = {0 : "Vineeth",1 : "Pranav"}
def videoFaceDet():
	names='Gaurav'
	count=0
	#capture video
	

	#Cascade Classifier
	
	faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

	#continuously processes video feed and displays in window until Q is pressed
	cap=cv2.VideoCapture('testing.mp4')
	while True:
		
		#the read function gives two outputs. The check is a boolean function that returns if the video is being read
		check, frame = cap.read()
		grayImg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		
		faces=faceCascade.detectMultiScale(grayImg, scaleFactor=1.5, minNeighbors=5)
		
		#superimposes a rectangle for all the detected images in the frame
		#(x,y) is the top left corner, (x+w, y+h) is the bottom right corner
		#(0,255,0) is colour green and 3 is the thickness of the rectangle edges

		for x, y, w, h in faces:
			frame=cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

		for face in faces:
			(x,y,w,h)=face
			roi_gray=grayImg[y:y+w, x:x+h]
			label,confidence=face_recognizer.predict(roi_gray)
			# print(confidence)
			fr.draw_rect(frame,face)
			predicted_name=name[label]
			if confidence < 68:
				fr.put_text(frame,predicted_name,x,y)
				if names!=predicted_name:
					names=predicted_name
					count+=1


			# # print("confidence:",confidence)
	  #       # print("label:",label)
	  #       fr.draw_rect(frame,face)
	  #       predicted_name=name[label]



		#window displaying the processed image
		cv2.imshow("Capturing", frame)
		key=cv2.waitKey(1)
		if key==ord('q'):
			break
		
	
	#Closes video window
	cv2.destroyAllWindows()
	
	#releases the video feed from the webcam/file
	cap.release()
	print("Total no.of people from previous video :",count)
videoFaceDet()


