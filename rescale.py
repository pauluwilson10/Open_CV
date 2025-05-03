import cv2 as cv

img=cv.imread("Photos/cat.jpg")
cv.imshow("cat",img)

def rescaleFrame(frame,scale=0.75):
    #works for videos,live videos and imagee
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_img=rescaleFrame(img)
cv.imshow("resized_cat",resized_img)


#This only works for live videos
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


#reading videos
capture=cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue,frame=capture.read()

    frame_resized=rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow("Video resized",frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitkey(0)