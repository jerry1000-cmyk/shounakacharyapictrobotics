import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Abhijit\Desktop\ROBOTICS CLUB\OpenCV\Photos\park.jpg")

cv.imshow("Original" , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",gray)

blur = cv.GaussianBlur(img , (3,3) , cv.BORDER_DEFAULT)
cv.imshow("Blurred" , blur)

canny = cv.Canny(img ,125,175)
cv.imshow("Edges",canny)


def translate(img , x , y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img , transmat , dimensions)

translated = translate(img , 100,0)
cv.imshow('Translated',translated)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img , 180)
cv.imshow("Rotated",rotated)

flip = cv.flip(img , 1)
# flip 0 is flip around horizontal axis
#flip 1 is flip around vertical axis ie mirror image
#flip -1 is both vertical and horizontal



cv.imshow("FLIIPED", flip)
      



cv.waitKey(0)