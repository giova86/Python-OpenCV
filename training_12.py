import cv2
import numpy as np
import os
print(os.getcwd())
print(os.listdir())

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        mycolorImage = np.zeros((512, 512, 3), np.uint8)

        mycolorImage[:] = [blue, green, red]
        print(mycolorImage)
        cv2.rectangle(mycolorImage, (0,0), (512,70), (0, 0, 0), -1 )
        font = cv2.FONT_HERSHEY_SIMPLEX
        strRGB = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(mycolorImage, strRGB, (100, 50), font, 1.5, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('color', mycolorImage)


img = cv2.imread('demo.jpeg')
#img = cv2.resize(img, (512, 512))
cv2.imshow('Image_test', img)
points = []
cv2.setMouseCallback('Image_test', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
