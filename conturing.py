import cv2 as cv
import numpy as np


img = cv.imread('data/Photos/cats.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

############
#  BASIC 
############

#create CANNY image
canny = cv.Canny(img, 125, 175)
cv.imshow('',canny)
cv.waitKey()

#take edges as input and give a LIST of contours as outputs

#1st: choose the method
# cv.RETR_EXTERNAL for external contours
# CV.RETR_LIST for all contours
# CV.RETR_TREE for hierarchical contours

#2nd: choose the approximation
# cv.CHAIN_APPROX_NONE
# cv.CHAIN_APPROX_SIMPLE

contours, hierarchies = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contour)) #2794



##############
# WITH BLUR
##############

# basic blurring with a kernel size of 5,5
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny_blur = cv.Canny(blur, 125, 175)
cv.imshow('',canny_blur)
cv.waitKey()

contours, hierarchies = cv.findContours(canny_blur,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours)) #380


##############
# WITH THRESHOLD
##############

# if value<125 set 0 (white) else set 255 (black)
thresh, bin_img = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('',bin_img)
cv.waitKey()

contours, hierarchies = cv.findContours(bin_img,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours)) #839


##############
# DRAW CONTOURS
##############

blank = np.zeros(img.shape)

#drawContours( on , from_list , how much?, color)
cv.drawContours(blank, contours, -1, (0,0,255))

cv.imshow('',blank)
cv.waitKey()




