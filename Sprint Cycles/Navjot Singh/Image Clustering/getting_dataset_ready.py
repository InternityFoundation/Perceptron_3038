import face_recognition
import cv2
import os
import glob
from imutils import paths
import pickle
from tqdm import tqdm

#image_paths=list(paths.list_images("dataset"))
knownEncodings=[]
knownNames=[]


for name in glob.glob("folder/*"):
    #os.path.join(path,f) for f in os.listdir(name))
    image_paths = [os.path.join(name,f) for f in os.listdir(name)]
    for (i,imagePath) in enumerate(image_paths):
        print("[INFO] processing image {}/{}".format(i + 1,len(image_paths)))
        Name = (os.path.split(imagePath)[0])
        name = Name.split('\\')[-1]
        img=cv2.imread(imagePath)
        rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        boxes=face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)
        for en in encodings:
            knownEncodings.append(en)
            knownNames.append(name)


data = {"encodings": knownEncodings, "names": knownNames}
f = open('E:\Python\ML\emb.picke', "wb")
f.write(pickle.dumps(data))
f.close()