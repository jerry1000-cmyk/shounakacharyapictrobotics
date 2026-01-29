import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3) , dtype='uint8')

cv.rectangle(blank , (0,0) , (250,250) , (0,255,0) , thickness = -1)
cv.rectangle(blank , (250,0) , (500,250) , (0,0,255) , thickness = -1)
cv.rectangle(blank , (0,250) , (250,500) , (255,0,0) , thickness = -1)
cv.rectangle(blank , (250,250) , (500,500) , (0,255,255) , thickness = -1)
cv.imshow('blank' , blank)



cv.waitKey(0)
