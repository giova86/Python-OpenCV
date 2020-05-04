import cv2

video = cv2.VideoCapture(0)

def make_1080p():
    video.set(3, 1920)
    video.set(4, 1080)

def make_720p():
    video.set(3, 1280)
    video.set(4, 720)

def make_480p():
    video.set(3, 640)
    video.set(4, 480)

def change_res(width, height):
    video.set(3, width)
    video.set(4, height)

make_1080p()

while True:
    ret, frame = video.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
