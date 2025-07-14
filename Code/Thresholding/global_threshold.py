import os
import cv2

# Semantic segmentation foreshadowing !
img = cv2.imread(os.path.join('..\\..\\data', 'Screenshot(635).png'))
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binImg = cv2.threshold(grayImg, 50, 255, cv2.THRESH_BINARY)
cleanImg = cv2.blur(binImg, (10, 10))
# Redo thresholding after blurring why?
ret, binImg = cv2.threshold(cleanImg, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('Og', img)
cv2.imshow('Thresholded Image', binImg)
cv2.waitKey(0)