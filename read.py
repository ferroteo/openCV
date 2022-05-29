import cv2

##########
# IMAGES 
##########

#imput
img = cv2.imread("data\Photos\cat.jpg")

#output
cv2.imshow('cat',img)
cv2.waitKey(0)



##########
# VIDEOS 
##########

#input from webcam
capture = cv2.VideoCapture(0)
#imput from file
capture = cv2.VideoCapture("data\Videos\dog.mp4")

#output
while True:
    isTrue, frame = capture.read()
    cv2.imshow('dog video',frame)

    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
#close output
capture.release()
cv2.destroyAllWindows()






