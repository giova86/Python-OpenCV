# PoseEstimationMin

import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

mp_holistic = mp.solutions.holistic
#holistic = mp_holistic.Holistic()

#mp_face_mesh = mp.solutions.face_mesh
#face_mesh = mp_face_mesh.FaceMesh()

mp_drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(0)
#cap.set(3,640)
#cap.set(4,480)
pTime = 0



with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1) as holistic:

    while True:
        success, img = cap.read()
        img.flags.writeable = False
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        results2 = holistic.process(imgRGB)
        print(results2.face_landmarks)
        #results = face_mesh.process(imgRGB)

        #print(results2.pose_landmarks)

        mpDraw.draw_landmarks(img, results2.face_landmarks, mp_holistic.FACEMESH_TESSELATION)


        mpDraw.draw_landmarks(
                img,
                results2.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles
                .get_default_pose_landmarks_style())

        mpDraw.draw_landmarks(
                img,
                results2.left_hand_landmarks,
                mp_holistic.HAND_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles
                .get_default_pose_landmarks_style())
        mpDraw.draw_landmarks(
            img,
            results2.right_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles
                .get_default_pose_landmarks_style())

        # if results.multi_face_landmarks:
        #     for face_landmarks in results.multi_face_landmarks:
        # mpDraw.draw_landmarks(
        #     img,
        #     results2.face_landmarks,
        #     mp_holistic.FACE_CONNECTIONS,
        #     # landmark_drawing_spec=None,
        #     # connection_drawing_spec=mp_drawing_styles
        #     #     .get_default_face_mesh_tesselation_style())
        # )
        # if results.pose_landmarks:
        #     mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        #     for id, lm in enumerate(results.pose_landmarks.landmark):
        #         if id in [12,11]:
        #             #print(lm.x*img.shape[0])
        #             cv2.circle(img, (int(lm.x*img.shape[1]), int(lm.y* img.shape[0])), 30, (255,0,255), -1)

        cTime = time.time()
        fps =1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {str(int(fps))}', (10,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255), 3)
        cv2.imshow("Image",  img)

        cv2.waitKey(1)
