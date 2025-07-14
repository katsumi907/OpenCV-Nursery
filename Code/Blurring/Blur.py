import os
import cv2

def resizeFrame (inputImg, scaling_factor):
    resizedFrame = cv2.resize(inputImg, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_LINEAR)
    return resizedFrame

absolute_path = os.path.abspath('daCatto.jpg')
image_path = os.path.join(absolute_path, '..\\..\\..\\data\\blur_meme.jpg')

scale_down = 0.7


plane = cv2.imread(image_path)
kernel_size = 11
blurFly = cv2.blur(plane, (kernel_size, kernel_size))
gaussBlurrFly  = cv2.GaussianBlur(plane, (kernel_size, kernel_size), 5)
medianBlurrFly = cv2.medianBlur(plane, kernel_size)

cv2.imshow('I\'m out', resizeFrame(plane, scale_down))
cv2.imshow("Blurry", resizeFrame(blurFly, scale_down))
cv2.imshow("Gaussian Blurry", resizeFrame(gaussBlurrFly, scale_down))
cv2.imshow("Median Blurry", resizeFrame(medianBlurrFly, scale_down))
cv2.waitKey(0)