import os
import cv2 as cv
import numpy as np

people = ["Ben Afflek" , "Elton John" , "Jerry Seinfield" , "Madonna","Mindy Kaling"]

dir = r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\Faces\train"
haar_cascade = cv.CascadeClassifier(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\haar_face.xml")
features = []
labels = []

def create_train():
  for person in people:
     path = os.path.join(dir,person)
     label = people.index(person)
     
     for img in os.listdir(path):
         img_path = os.path.join(path,img)
         img_array = cv.imread(img_path)
         gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

         faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors=4)

         for (x,y,w,h) in faces_rect:
            faces_roi = gray[y:y+h , x:x+w]
            features.append(faces_roi)
            labels.append(label)


create_train()
features = np.array(features,dtype='object')
labels = np.array(labels)

faces_recognizer = cv.face.LBPHFaceRecognizer_create()

faces_recognizer.train(features , labels)

faces_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)

