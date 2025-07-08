import os

import cv2

proj_path = "C:\\Users\\maria\\PycharmProjects\\PythonProject"

# Read image
image_path = os.path.join(proj_path, 'data', 'daCatto.jpg')

img = cv2.imread(image_path)

# Write image

#cv2.imwrite(os.path.join(proj_path, 'data', 'daCattoOut.jpg'), img)

# Visualize image

cv2.imshow('Dis a pic', img)

# Waits 0->indefinitely (while displaying image) for any button to be pressed
cv2.waitKey(0)

