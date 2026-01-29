import cv2 as cv
import numpy as np


img = cv.imread(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\Photos\park.jpg")
blank =  np.zeros(img.shape[:2],dtype="uint8")


b,g,r = cv.split(img)
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue" , blue)  
cv.imshow("Green" , green)
cv.imshow("Red" , red)

#if you want to see the actual colour chanel instaed of just its respective intensity you can overlay a blank img on top of the splitted img

# Light is where the concentration is high and black is where concentration of that colour is low
merged = cv.merge([b,g,r])
cv.imshow("Merged",merged)



cv.waitKey(0)