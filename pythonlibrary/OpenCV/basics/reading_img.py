import cv2 as cv

img = cv.imread("Cat.jpg",)   # Just the filename if you're in the same folder
#this read the image 
#if you have a lage image it will go offscreen

cv.imshow('Cat',img)
# this shows the image

cv.waitKey(0)