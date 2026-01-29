import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\Photos\cats.jpg")
cv.imshow("Original",img)

#the number (3,3) is the kernal window basically how many divisions will be there where the effect will be applied
#high kernal size = more blur
#kernal size should be odd

#Averaging
avg = cv.blur(img,(3,3))
cv.imshow("Average",avg)

#Gaussian Blur
#more natural but less blur
gauss = cv.GaussianBlur(img , (7,7) , 0)

cv.imshow("Gausian",gauss)

#Median Blur 
# Very effective , only used when the camera was like very fucked up or you need to run a model and dont need high noise

median = cv.medianBlur(img , 7)
cv.imshow("Median",median)

#Bilateral Blur
#Used in CV projects as it reduces edges

bilateral = cv.bilateralFilter(img , 10 , 25 ,25)
cv.imshow("Bilateral",bilateral)




cv.waitKey(0)