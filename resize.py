from configparser import Interpolation
import cv2

img = cv2.imread("data\Photos\cat_large.jpg")
capture = cv2.VideoCapture("data\Videos\dog.mp4")


################
#   RESCALE
################

def FrameRescale(frame,scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width,height)

    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

#for IMAGES
cv2.imshow("resized image", FrameRescale(img))

#fro VIDEOS
while True:
    isTrue, frame = capture.read()

    rescaled_frame = FrameRescale(frame)
    cv2.imshow('video risized',rescaled_frame)

    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
capture.release()
cv2.destroyAllWindows()


#for LIVE videos
def ChangRes(width,height):

    capture.set(3,width)
    capture.set(4,height)



