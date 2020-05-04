import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 100)
cap.set(4, 100)

while True:
    ret, frame = cap.read()

    text = 'Width: ' + str(int(cap.get(3))) + ' - Height: ' + str(int(cap.get(4)))
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame, text, (10,50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Video Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


