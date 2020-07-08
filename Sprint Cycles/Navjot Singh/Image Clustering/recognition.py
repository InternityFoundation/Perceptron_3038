

import pickle
import cv2
import numpy as np
import imutils
from sklearn.cluster import DBSCAN
from imutils import build_montages
import os
from tqdm import tqdm
import face_recognition

#data = pickle.loads(open(args["encodings"], "rb").read())
data = pickle.loads(open("emb.picke", "rb").read())
cap=cv2.VideoCapture(r'E:\Python\Lecture_10\testing_video.mp4')

while True:
    ret,frame=cap.read()
    if ret is False:
        cap.release()
        break
    #frame=cv2.flip(frame,1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb,model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    for e in encodings:
        matches = face_recognition.compare_faces(data["encodings"],e)
        name = "Unknown"
        if True in matches:
            indx=[i for (i,b) in enumerate(matches) if b]
            counts = {}
            for i in indx:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            
            name = max(counts, key=counts.get)
        names.append(name)
    
    for ((top, right, bottom, left), name) in zip(boxes, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
    cv2.imshow("me",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()