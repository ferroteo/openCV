import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

#create a black filled rectangle an circle
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)


###########
#  AND
###########

bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow('',bit_and)
cv.waitKey()


###########
#  OR
###########

bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow('',bit_or)
cv.waitKey()


###########
#  AND
###########

bit_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('',bit_xor)
cv.waitKey()


###########
#  AND
###########

bit_not = cv.bitwise_not(circle)
cv.imshow('',bit_not)
cv.waitKey()



############
#  MASKING 
############

img = cv.imread('data/Photos/cats.jpg')
blank = np.zeros(img.shape[:2],dtype='uint8')

#NB: create a white circle where we want to see the image
#NB: can use all the shapes you want!
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv.imshow('',mask)
cv.waitKey()

img_masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('',img_masked)
cv.waitKey()