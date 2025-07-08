import cv2

# Read webcam
webcam = cv2.VideoCapture(0) # Takes webcam index, so 0 for you PEASANT

# Visualize webcam
while True:
    ret, frame = webcam.read()
    cv2.imshow('Your Pretty Face', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'): # Once again, number here is inverse frame rate (time(ms)/frames)
        break

webcam.release()
cv2.destroyAllWindows()

