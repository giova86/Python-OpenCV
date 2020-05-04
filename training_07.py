import numpy as np
import cv2
#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)
img = cv2.line(img, (0,0), (55,55), (147, 96, 44), 10) # 44, 96, 147
img = cv2.arrowedLine(img, (0,155), (255,155), (255, 0, 0), 5)
img = cv2.rectangle(img, (284, 50), (510, 128), (0, 0, 255), 10)

# (xc, yc), radius, color, thickness/full
img = cv2.circle(img, (247, 63), 63, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 400), font, 4, (0, 255, 255), 10, cv2.LINE_AA)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
