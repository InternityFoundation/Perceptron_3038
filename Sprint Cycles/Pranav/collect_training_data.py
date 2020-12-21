import cv2

def generate_dataset(img, id, img_id):
    cv2.imwrite("signs/user."+str(id)+"."+str(img_id)+".jpg", img)
    


def draw_boundary(img, faceCascade, scaleFactor, minNeighbors, color, text):
    
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    features = faceCascade.detectMultiScale(grayImg, scaleFactor=1.5, minNeighbors=5)
    coords = []
    
    for x, y, w, h in features:
        features=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
        coords = [x, y, w, h]
    return coords

def detect(img, faceCascade, img_id):
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")
    
    if len(coords)==4:
        
        roi_img = img[coords[1]:coords[1]+coords[3], coords[0]:coords[0]+coords[2]]
        
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)

    return img
#Cascade Classifier
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

img_id=0
while True:
    _, img = cap.read()
    img = detect(img, faceCascade, img_id)
    cv2.imshow("Capturing", img)
    img_id += 1
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
	
#Closes video window
cv2.destroyAllWindows()
#releases the video feed from the webcam/file
cap.release()

