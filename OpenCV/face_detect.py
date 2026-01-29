import cv2 as cv

img = cv.imread(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\Photos\group 2.jpg")

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\haar_face.xml")

face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)

#this will apply that xml file we coppied find all faces and detect the rectangle in which face is detected and give it to us in form of a list 
# which is face_detect

print(f"Number of faces found = {len(face_rect)}")

for (x,y,w,h) in face_rect:
    cv.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0) , thickness=2)
cv.imshow("Face Detected" , img)
cv.waitKey(0)
