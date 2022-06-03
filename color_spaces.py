import cv2 as cv

img = cv.imread('data/Photos/park.jpg')
cv.imshow('',img)
cv.waitKey()


############
#  GRAY
############

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('',gray)
cv.waitKey()


############
#  HSV
############
#huge saturation values

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('',hsv)
cv.waitKey()


############
#  LAB
############

lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('',lab)
cv.waitKey()


############
#  RGB
############

rgb = cv.cvtColor(img,cv.COLOR_BGRRGB)
cv.imshow('',rgb)
cv.waitKey()

