import cv2
import numpy as np


#BLANK image
blank = np.zeros((500,500,3),dtype='uint8')
cv2.imshow('Blank image',blank)


##################
#  CHANGE COLOR
##################

#based on BGR scale 

#set green 
blank[:] = 0,255,0
cv2.imshow('green image',blank)

#set red 
blank[:] = 0,0,255
cv2.imshow('red image',blank)

#draw basic SHAPES
blank[50:450 , 0:50] = 0,0,0
cv2.imshow('black shape',blank)



##################
#  DRAW SHAPES
##################

blank = np.zeros((500,500,3),dtype='uint8')

#______________________
# 1. RECTANGLE/SQUARE :

# on , from , to , color , thickness
cv2.rectangle(blank , (10,10) , (450,450), (0,250,0) , thickness=2)
cv2.imshow(' ',blank)

#NB: if we want filled shapoe we use
cv2.rectangle(blank , (10,10) , (450,450), (0,250,0) , thickness=cv2.FILLED)
cv2.imshow(' ',blank)

#________________________
#2. CIRCLE :

# on , center , radius , color , thickness
cv2.circle(blank , (blank.shape[1]//2,blank.shape[0]//2) , 30, (250,0,0) , thickness=2)
cv2.imshow(' ',blank)

#__________________________
#3. STRAIGHT LINE :

# on , from , to , color , thickness
cv2.line(blank , (10,10) , (450,450) , (0,0,255) , thickness=2)
cv2.imshow(' ',blank)


##################
#  WRITE TEXT  
##################

# on, text , left margin coord , format , size , color , thickness
cv2.putText(blank, 'hello world!' , (100,100) ,
         cv2.FONT_HERSHEY_COMPLEX, 5 , (255,255,255) , 2)
cv2.imshow(' ',blank)
cv2.waitKey(0)



