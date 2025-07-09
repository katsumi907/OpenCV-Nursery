import os
import cv2


# I've decided to write a method to detect pixel coordinates for the sake of cropping because I'm lazy.
def click_event(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONDOWN:
      print(f'({x},{y})')
      cv2.putText(img, f'({x},{y})',(x,y),
      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


absolute_path = os.path.abspath('daCatto.jpg')
image_path = os.path.join(absolute_path, '..\\..\\..\\data\\daCatto.jpg')
img = cv2.imread(image_path)
print(img.shape)

# Coordinates are as follows -> [y1:y2, x1:x2] OR [height, width] (It's weird ik, you'll get used to it)
cropped_img = img[109:680, 33:699]

cv2.imshow("Original", img)

# Binding click function to specific window (Original image window in this case)
cv2.setMouseCallback('Original', click_event)

cv2.imshow("Crop", cropped_img)

cv2.waitKey(0)