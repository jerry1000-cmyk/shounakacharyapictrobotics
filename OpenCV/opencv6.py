import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\Photos\cats.jpg")
# cv.imshow("Original",img)

blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv.circle(blank , (img.shape[1]//2 , img.shape[0]//2) ,100, (255,255,255) , -1)
cv.imshow("Mask",mask)

#size of your mask must be same size as the image for the coordinates to match
masked = cv.bitwise_and(img,img,mask=mask)

cv.imshow("Masked" , masked)

cv.waitKey(0)