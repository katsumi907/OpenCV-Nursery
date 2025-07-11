import cv2
import time
import numpy as np

webcam = cv2.VideoCapture(0) # Takes webcam index, so 0 for you PEASANT

delayFlag, displayFlag = 0, 0
y = 300
x = -25
scale_down_fac = 0.6

def sizeDownFrame (inputImg, scale_down_factor):
    smallFrame = cv2.resize(inputImg, None, fx=scale_down_factor, fy=scale_down_factor, interpolation=cv2.INTER_LINEAR)
    return smallFrame

while True:
    ret, frame = webcam.read()
    # Mirroring/flipping the frame horizontally. Can flip horizontally, vertically or both. Check axis values.
    frame = np.flip(frame, axis=1)
    # Declared multiple frames hoping that maybe by "separating" them I could read the video feed in parallel. Guess not.
    #ret2, frame2 = webcam.read()
    #ret3, frame3 = webcam.read()
    #ret4, frame4 = webcam.read()

    # Color-converted frames
    BToRFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    BGR2GrayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    BGRToHSVFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Window names
    regWindow = 'Your Pretty Face'
    B2RWin = 'Oh look, you\'re a smurf!'
    BGR2GrayWin = "Now you're in the 50's"
    B2HSVWin = "Ok, it's time to stop."

    if delayFlag == 0:
        #time.sleep(2)
        cv2.namedWindow(regWindow) # Create a named window
        cv2.moveWindow(regWindow, x, y)  # Move it to (x, y)
        cv2.imshow(regWindow, sizeDownFrame(frame, scale_down_fac))
        time.sleep(1)
        cv2.namedWindow(B2RWin)
        cv2.moveWindow(B2RWin, x + 380, y)
        cv2.imshow(B2RWin, sizeDownFrame(BToRFrame, scale_down_fac))
        time.sleep(0.5)
        cv2.namedWindow(BGR2GrayWin)
        cv2.moveWindow(BGR2GrayWin, x + 760, y)
        cv2.imshow(BGR2GrayWin, sizeDownFrame(BGR2GrayFrame, scale_down_fac))
        time.sleep(0.5)
        cv2.namedWindow(B2HSVWin)
        cv2.moveWindow(B2HSVWin, x + 1140, y)
        cv2.imshow(B2HSVWin, sizeDownFrame(BGRToHSVFrame, scale_down_fac))

        delayFlag = 1

    #time.sleep(2)
    cv2.namedWindow(regWindow) # Create a named window
    cv2.moveWindow(regWindow, x, y)  # Move it to (x, y)
    cv2.imshow(regWindow, sizeDownFrame(frame, scale_down_fac))
    cv2.namedWindow(B2RWin)
    cv2.moveWindow(B2RWin, x + 380, y)
    cv2.imshow(B2RWin, sizeDownFrame(BToRFrame, scale_down_fac))
    cv2.namedWindow(BGR2GrayWin)
    cv2.moveWindow(BGR2GrayWin, x + 760, y)
    cv2.imshow(BGR2GrayWin, sizeDownFrame(BGR2GrayFrame, scale_down_fac))
    cv2.namedWindow(B2HSVWin)
    cv2.moveWindow(B2HSVWin, x + 1140, y)
    cv2.imshow(B2HSVWin, sizeDownFrame(BGRToHSVFrame, scale_down_fac))

    #cv2.namedWindow(regWindow)
    #cv2.namedWindow(B2RWin)
    #cv2.namedWindow(BGR2GrayWin)
    #cv2.namedWindow(B2HSVWin)

    #cv2.moveWindow(regWindow, x, y)  # Move it to (x, y)
    #cv2.moveWindow(B2RWin, x + 380, y)
    #cv2.moveWindow(BGR2GrayWin, x + 760, y)
    #cv2.moveWindow(B2HSVWin, x + 1140, y)

    # Scaling factors for resizing
    #sizeDownImg = cv2.resize(frame, None, fx=scale_down_fac, fy=scale_down_fac, interpolation=cv2.INTER_LINEAR)
    #sizeDownBToR = cv2.resize(BToRFrame, None, fx=scale_down_fac, fy=scale_down_fac, interpolation=cv2.INTER_LINEAR)
    #sizeDownBGR2Gray = cv2.resize(BGR2GrayFrame, None, fx=scale_down_fac, fy=scale_down_fac, interpolation=cv2.INTER_LINEAR)
    #sizeDownBGRToHSV = cv2.resize(BGRToHSVFrame, None, fx=scale_down_fac, fy=scale_down_fac, interpolation=cv2.INTER_LINEAR)
#    cv2.imshow('Your Pretty Face', frame)
#    cv2.imshow('Oh look, you\'re a smurf!', BToRFrame)



    #cv2.imshow(regWindow, sizeDownImg)
    #cv2.imshow(B2RWin, sizeDownBToR)
    #cv2.imshow(BGR2GrayWin, sizeDownBGR2Gray)
    #cv2.imshow(B2HSVWin, sizeDownBGRToHSV)


    if cv2.waitKey(10) & 0xFF == ord('q'): # Once again, number here is inverse frame rate (time(ms)/frames)
        break

webcam.release()
cv2.destroyAllWindows()

# Comment here since Github hates me:
# Next step: define functions to avoid code repetition & try out more color spaces!
# Drafts: read mkv files instead of mp4 using ffmpeg, and have openCV windows display coordinates & RGB values.