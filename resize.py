from configparser import Interpolation
import cv2

img = cv2.imread("data\Photos\cat_large.jpg")
capture = cv2.VideoCapture("data\Videos\dog.mp4")


################
# RESIZE VIDEO
################

def FrameRescale(frame,scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width,height)

    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)


while True:
    isTrue, frame = capture.read()

    rescaled_frame = FrameRescale(frame)
    cv2.imshow('video risized',rescaled_frame)

    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
capture.release()
cv2.destroyAllWindows()


#################
# RESCALE IMAGE
#################

#left 17.31



