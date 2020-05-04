import cv2

img_bw  = cv2.imread('demo.jpeg',0)
img_cl  = cv2.imread('demo.jpeg',1)

cv2.imshow('B&W Image',img_bw)
cv2.imshow('Color Image',img_cl)


cv2.waitKey(0)
cv2.destroyAllWindows()
