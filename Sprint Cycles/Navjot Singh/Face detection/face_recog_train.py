import os
import numpy as np 
from PIL import Image
import cv2


recog = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'

def getImageswithID(path):
	imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
	faces = []
	Names = []

	for imgpath in imagePaths:
		faceImg = Image.open(imgpath)
		faceNp = np.array(faceImg,'uint8')
		Name = (os.path.split(imgpath)[-1].split('_')[0])
		
		faces.append(faceNp)
		Names.append(Name)
		cv2.imshow('training',faceNp)
		cv2.waitKey(10)
	return Names, faces

Names ,faces = getImageswithID(path)
Names=[0]*len(faces)
recog.train(faces,np.array(Names))
recog.write('trainingData1.yml')
cv2.destroyAllWindows()

