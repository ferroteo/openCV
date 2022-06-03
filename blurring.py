import cv2 as cv
import numpy as np


img = cv.imread('data/Photos/park.jpg')
cv.imshow('',img)
cv.waitKey()


##############
#  AVARAGE
##############

# The pixel take the avarage value of all the pixels
# inside the sorrunding kernel window

avarage = cv.blur(img, (3,3))

cv.imshow('',avarage)
cv.waitKey()


##############
#  MEDIAN
##############

# The pixel take the median value of all the pixels
# inside the sorrunding kernel window

#NB: very useful to reduce noise

median = cv.medianBlur(img, 3)

cv.imshow('',median)
cv.waitKey()


##############
#  GAUSSIAN
##############

# The pixel take the weighted avarage value of all the 
# pixels inside the sorrunding kernel window

# weight based on .. 

#NB: last parameter rapresents the variance
gauss = cv.GaussianBlur(img, (3,3) ,0 )

cv.imshow('',gauss)
cv.waitKey()


##############
#  BILATERAL
##############

# The pixel take the median value of all the pixels
# inside the sorrunding kernel window

#NB: very useful for AI projects

# ( on , diameter, color_sigma ,space_sigma )
bil = cv.bilateralFilter(img, 5, 15, 15)

cv.imshow('',bil)
cv.waitKey()