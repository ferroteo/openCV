import cv2


#################
#  RESIZE
#################

img = cv2.imread("data\Photos\park.jpg")

#basic
resized = cv2.resize(img, (500,500))
cv2.imshow('',resized)
cv2.waitKey(0)

#advanced:
# shrink image -> cv2.INTER_AREA
# enlarge image -> cv2.LINEAR  cv2.CUBIC
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
cv2.imshow('',resized)
cv2.waitKey(0)


#######################
#  CROPPING / PATCHING
#######################

crop = img[50:200,200:400]
cv2.imshow('',crop)
cv2.waitKey(0)




##############
# COLOR SCALE  
##############

#______________________
#1. basic BGR scale
cv2.imshow('',img)
cv2.waitKey(0)

#_______________________
#2. gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('',gray)
cv2.waitKey(0)


#_______________________
#2. RGB scale
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('',rgb)
cv2.waitKey(0)


##############
# BLURRING 
##############

# on , kernel size (conv patch) , border type
blur = cv2.GaussianBlur(img, (5,5) , cv2.BORDER_DEFAULT)
cv2.imshow('',blur)
cv2.waitKey(0)


#################
# EDGE DETECTION 
#################

#use a basic algorithm called "CANNY"
canny = cv2.Canny(img, 125,175)
cv2.imshow('',canny)
cv2.waitKey(0)

#now on the blurred image to be more precise!
canny = cv2.Canny(blur, 125,175)
cv2.imshow('',canny)
cv2.waitKey(0)



#################
# DILATING EDGES
#################

#perform dialationg basad on the edge detected
dilated = cv2.dilate(canny, kernel=(7,7), iterations = 3)
cv2.imshow('',dilated)
cv2.waitKey(0)

#################
# ERODING EDGES
#################

#opposite of dilating
eroded = cv2.erode(dilated, kernel=(7,7), iterations = 3)
cv2.imshow('',eroded)
cv2.waitKey(0)


