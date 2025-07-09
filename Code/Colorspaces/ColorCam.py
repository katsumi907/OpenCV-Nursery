import cv2

webcam = cv2.VideoCapture(0) # Takes webcam index, so 0 for you PEASANT

while True:
    ret, frame = webcam.read()
    cursedFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('Your Pretty Face', frame)
    cv2.imshow('Oh look, you\'re a smurf!', cursedFrame)
    if cv2.waitKey(30) & 0xFF == ord('q'): # Once again, number here is inverse frame rate (time(ms)/frames)
        break

webcam.release()
cv2.destroyAllWindows()