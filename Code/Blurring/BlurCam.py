import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    # Mirroring/flipping the frame horizontally. Can flip horizontally, vertically or both. Check axis values.
    frame = np.flip(frame, axis=1)
    blurFrame = cv2.medianBlur(frame, 9)

    cv2.imshow('Blurry ME!', blurFrame)

    if cv2.waitKey(10) & 0xFF == ord('q'):  # Once again, number here is inverse frame rate (time(ms)/frames)
        break

webcam.release()
cv2.destroyAllWindows()