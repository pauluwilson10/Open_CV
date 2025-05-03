import cv2 as cv

img=cv.imread("Photos/park.jpg")
cv.imshow("boston",img)

#Converting to gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

#Edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow("Canny edges",canny)

#dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated",dilated)

#Eroding
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)

#Resize 
resized=cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
cv.imshow("resized",resized)
#Cropping
cropped=img[50:200,200:400]
cv.imshow("cropped",cropped)
cv.waitKey(0)