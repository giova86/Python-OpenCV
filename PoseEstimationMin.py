# PoseEstimationMin

import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            if id in [12,11]:
                print(lm.x*img.shape[0])
                cv2.circle(img, (int(lm.x*img.shape[1]), int(lm.y* img.shape[0])), 30, (255,0,255), -1)

    cTime = time.time()
    fps =1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {str(int(fps))}', (10,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.imshow("Image", img)

    cv2.waitKey(1)
