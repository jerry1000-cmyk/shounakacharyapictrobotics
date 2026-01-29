import numpy as np
import cv2 as cv


people = ["Ben Afflek" , "Elton John" , "Jerry Seinfield" , "Madonna","Mindy Kaling"]
haar_cascade = cv.CascadeClassifier(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\haar_face.xml")

features = np.load('features.npy',allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\Faces\val\ben_afflek\1.jpg")
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

cv.imshow("Person" , gray)

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label , confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {people[label]} with a confidence of {100-confidence}%")