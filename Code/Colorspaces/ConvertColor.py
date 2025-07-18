import os
from base64 import b32encode
import time
import cv2
# Figure out how to import a single method without running the whole other file, Bozo
# from ColorCam import sizeDownFrame

def sizeDownFrame (inputImg, scale_down_factor):
    smallFrame = cv2.resize(inputImg, None, fx=scale_down_factor, fy=scale_down_factor, interpolation=cv2.INTER_LINEAR)
    return smallFrame
# Learn to display the coordinates + RGB values of mouse-hovered pixel
absolute_path = os.path.abspath('daCatto.jpg')
image_path = os.path.join(absolute_path, '..\\..\\..\\data\\daCatto.jpg')

scale_down = 0.5
# Positioning da windows
y = 250
x = -25

# Doing some color conversions
# There are plenty more color spaces. So feel free to check openCV documentation, but you won't will you?? Lazy ass :D
img = cv2.imread(image_path)
img_new = cv2.resize(img, (370, 749))
BToR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
BGR2Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
BGRToHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# "Declaring" the windows in order to be able to re-position them in a cleaner form
regWindow = "Dis A Cat"
B2RWin = "Dis A Cool Cat"
BGR2GrayWin = "Dis A Classic Cat"
B2HSVWin = "Dis A Cursed Cat"

cv2.namedWindow(regWindow)
cv2.moveWindow(regWindow, x, y)  # Move it to (x, y)
cv2.imshow(regWindow, sizeDownFrame(img, scale_down))
time.sleep(0.5)
cv2.namedWindow(B2RWin)
cv2.moveWindow(B2RWin, x+380, y)
cv2.imshow(B2RWin, sizeDownFrame(BToR, scale_down))
time.sleep(0.5)
cv2.namedWindow(BGR2GrayWin)
cv2.moveWindow(BGR2GrayWin, x+760, y)
cv2.imshow(BGR2GrayWin, sizeDownFrame(BGR2Gray, scale_down))
time.sleep(0.5)
cv2.namedWindow(B2HSVWin)
cv2.moveWindow(B2HSVWin, x+1140, y)
cv2.imshow(B2HSVWin, sizeDownFrame(BGRToHSV, scale_down))


# Resize the image & its sisters so they'd fit
#sizeDownImg = cv2.resize(img, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
#sizeDownBToR = cv2.resize(BToR, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
#sizeDownBGR2Gray = cv2.resize(BGR2Gray, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
#sizeDownBGRToHSV = cv2.resize(BGRToHSV, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)



# Old, worthless, windowless displays
#cv2.imshow('Dis A Cat', img)
#cv2.imshow('Dis A Cool Cat', BToR)
#cv2.imshow('Dis A Classic Cat', BGR2Gray)
#cv2.imshow('Dis A Cursed Cat', BGRToHSV)

cv2.waitKey(0)