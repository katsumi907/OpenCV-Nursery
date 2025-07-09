import os
import cv2


# Read video
absolute_path = os.path.abspath('robloxapp-20230518-1113027.wmv')
video_path = os.path.join(absolute_path, '..\\..\\..\\data\\robloxapp-20230518-1113027.wmv')

#proj_path = "C:\\Users\\maria\\PycharmProjects\\PythonProject"
#video_path = os.path.join(proj_path, 'data', 'robloxapp-20230518-1113027.wmv')

# Converting mkv to mp4 using ffmpeg cmd, research on this later!
#os.system("ffmpeg -i Friends_1x22_The_One_With_The_Ick.mkv -codec copy Friends_1x22_The_One_With_The_Ick.mp4")

vid = cv2.VideoCapture(video_path)

#os.system("ffmpeg -i vid -codec copy Friends_1x22_The_One_With_The_Ick.mp4")

# Visualize video

ret = True
while ret:
    # Reads frame from video file while video still has frames
    ret, frame = vid.read()
    if ret:
        cv2.imshow('Roblox Dance-Off', frame)
        # The smaller the number, the faster the frames (less wait, duh)
        cv2.waitKey(10)

vid.release()
cv2.destroyAllWindows()