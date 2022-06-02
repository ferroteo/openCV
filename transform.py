import cv2
import numpy as np


img = cv2.imread("data\Photos\park.jpg")
cv2.imshow('',img)
cv2.waitKey()


################
#   TRANSLATE
################

def translate(img,x,y):

    transMat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1],img.shape[0])

    return cv2.warpAffine(img, transMat, dim )

img_trans = translate(img,100,100)
cv2.imshow('',img_trans)
cv2.waitKey()

#NB:
# y>0 means down
# x>0 means right



################
#   ROTATION
################

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dim = (height,width) 

    return cv2.warpAffine(img, rotMat, dim )

img_rot = rotate(img,45)
cv2.imshow('',img_rot)
cv2.waitKey()

#NB: angle>0 means counter-clockwise



################
#   RESIZE
################

resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('',resized)
cv2.waitKey()


################
#   FLIP
################

flipped = cv2.flip(img, -1)
# 0 = vertically
# 1 = horizontally
# -1 = both vert ad horiz

cv2.imshow('',flipped)
cv2.waitKey()



################
#   CROPPING
################

cropped = img[200:400,300:500]

cv2.imshow('',cropped)
cv2.waitKey()