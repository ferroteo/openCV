import cv2 as cv
import numpy as np

img = cv.imread('data/Photos/park.jpg')
cv.imshow('',img)
cv.waitKey()


###############
#  SPLITTING
###############

b_img, g_img, r_img = cv.split(img)

#NB: each channel is one dimensional 

# draw in GRAY SCALE
cv.imshow('blue',b_img)
cv.imshow('green',g_img)
cv.imshow('red',r_img)
cv.waitKey()


#draw in respective COLOR SCALE
blank = np.zeros(img.shape[:2],dtype='uint8')

blue = cv.merge([b_img,blank,blank])
green = cv.merge([blank,g_img,blank])
red = cv.merge([blank,blank,r_img])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)
cv.waitKey()


###############
#  MERGING
###############

merged = cv.merge([b_img,g_img,r_img])