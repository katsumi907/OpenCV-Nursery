import os

import cv2


# Read image from path
# Adjusted os path reading to read relative path instead of hard-coding my own path
absolute_path = os.path.abspath('daCatto.jpg')
image_path = os.path.join(absolute_path, '..\\..\\..\\data\\daCatto.jpg')
#proj_path = os.chdir('..\\', absolute_path)

#print(proj_path)
print(image_path)


img = cv2.imread(image_path)

# Write image

#cv2.imwrite(os.path.join(proj_path, 'data', 'daCattoOut.jpg'), img)

# Visualize image

cv2.imshow('Dis a pic', img)

# Waits 0->indefinitely (while displaying image) for any button to be pressed
cv2.waitKey(0)

