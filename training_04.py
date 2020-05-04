import cv2, time

video = cv2.VideoCapture(0)
num_frames = 1

while True:
    num_frames += 1
    check, frame = video.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Capturing', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(num_frames)
video.release()
cv2.destroyAllWindows
