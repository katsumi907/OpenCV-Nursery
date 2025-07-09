import cv2

webcam = cv2.VideoCapture(0) # Takes webcam index, so 0 for you PEASANT


while True:
    ret, frame = webcam.read()

    # Color-converted frames
    BToRFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    BGR2GrayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    BGRToHSVFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Window names
    regWindow = 'Your Pretty Face'
    B2RWin = 'Oh look, you\'re a smurf!'
    BGR2GrayWin = "Now you're in the 50's"
    B2HSVWin = "Ok, it's time to stop."

    cv2.namedWindow(regWindow)
    cv2.namedWindow(B2RWin)  # Create a named window
    cv2.namedWindow(BGR2GrayWin)  # Create a named window
    cv2.namedWindow(B2HSVWin)

    y = 300
    x = -25
    cv2.moveWindow(regWindow, x, y)  # Move it to (x, y)
    cv2.moveWindow(B2RWin, x + 380, y)
    cv2.moveWindow(BGR2GrayWin, x + 760, y)
    cv2.moveWindow(B2HSVWin, x + 1140, y)

    # Scaling factors for resizing
    scale_down_factor = 0.6
    sizeDownImg = cv2.resize(frame, None, fx=scale_down_factor, fy=scale_down_factor, interpolation=cv2.INTER_LINEAR)
    sizeDownBToR = cv2.resize(BToRFrame, None, fx=scale_down_factor, fy=scale_down_factor, interpolation=cv2.INTER_LINEAR)
    sizeDownBGR2Gray = cv2.resize(BGR2GrayFrame, None, fx=scale_down_factor, fy=scale_down_factor, interpolation=cv2.INTER_LINEAR)
    sizeDownBGRToHSV = cv2.resize(BGRToHSVFrame, None, fx=scale_down_factor, fy=scale_down_factor, interpolation=cv2.INTER_LINEAR)
#    cv2.imshow('Your Pretty Face', frame)
#    cv2.imshow('Oh look, you\'re a smurf!', BToRFrame)

    cv2.imshow(regWindow, sizeDownImg)
    cv2.imshow(B2RWin, sizeDownBToR)
    cv2.imshow(BGR2GrayWin, sizeDownBGR2Gray)
    cv2.imshow(B2HSVWin, sizeDownBGRToHSV)

    if cv2.waitKey(30) & 0xFF == ord('q'): # Once again, number here is inverse frame rate (time(ms)/frames)
        break

webcam.release()
cv2.destroyAllWindows()