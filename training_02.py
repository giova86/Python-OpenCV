import cv2

scale_factor = 4

img  = cv2.imread('demo.jpeg',1)

img_scaled = cv2.resize(img,(int(img.shape[1]/scale_factor),
                             int(img.shape[0]/scale_factor)
                            )
                       )

cv2.imshow('Image',img_scaled)

cv2.waitKey(0)

cv2.destroyAllWindows()
