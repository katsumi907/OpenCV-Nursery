import os
import cv2

project_path = "C:\\Users\\maria\\PycharmProjects\\PythonProject"

img = cv2.imread(os.path.join(project_path, "data", "daCatto.jpg"))

# Mind that the dimension are entered in OPPOSITE order in which they're displayed in print shape
img_new = cv2.resize(img, (370, 749))

# Displays image size (x * y * 3), the 3 for 3 color channels?
print(img.shape)
print(img_new.shape)

cv2.imshow("Le Image", img)
cv2.imshow("Le Image 2", img_new)
cv2.waitKey(0)
