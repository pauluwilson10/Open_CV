import cv2 as cv

img=cv.imread("Photos/cats.jpg")
cv.imshow("cats",img)

#Averaging
average=cv.blur(img,(3,3))
cv.imshow("Average blur",average)

#Gaussian blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow("gaussian blur",gauss)

#Median blur
"""
not applicable to 5  and 7
"""
median=cv.medianBlur(img,3)
cv.imshow("median",median)

#Bilateral
Bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow("bilateral",Bilateral)




cv.waitKey(0)