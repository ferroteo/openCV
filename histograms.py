import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("data\Photos\cats.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('',gray)
cv.waitKey()


##############
#  BASIC
##############

# ( img_list, channel_list, mask , n_bins , value_range)
gray_hist = cv.calcHist([gray], [0], None, [256] , [0,256] )

#plot the histogram
plt.figure()
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#############
# WITH MASK
#############

blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('',mask)
cv.waitKey()

gray_hist = cv.calcHist([gray], [0], mask, [256] , [0,256] )

#plot the histogram
plt.figure()
plt.xlabel('bins')
plt.ylabel('pixels number')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey()



################
# WITH COLORS
################

plt.figure()

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256] , [0,256] )
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()