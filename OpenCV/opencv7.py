import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\Photos\cats.jpg")
blank = np.zeros(img.shape[:2],dtype="uint8")

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# cv.imshow("gray",gray)

threshholdvalue , threshimg = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY)
# cv.imshow("threshholded",threshimg)

adaptivethresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
# cv.imshow('Adapativethereshold' , adaptivethresh)

# laplacian method to find edges
#its result is like if you drew the image on a chalkboard or pencil

lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)


# Sobel method to find edges
sobelx = cv.Sobel(gray , cv.CV_64F,1,0)
sobely = cv.Sobel(gray , cv.CV_64F,0,1)
merged = cv.bitwise_or(sobelx,sobely)

cv.imshow("Sobel X",sobelx)
cv.imshow("Sobel Y",sobely)
cv.imshow("merged" , merged)




cv.waitKey(0)