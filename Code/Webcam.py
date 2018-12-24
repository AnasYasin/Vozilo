import cv2
import time
class Camera:

    def captureImage(self, name):
        temp=name
        name=name+'.png'
        cam = cv2.VideoCapture(0) #0 for cam 1, i.e laptop's builtin cam
        #time.sleep(1)
        ret, frame = cam.read()   # capturing image
        if ret != True:
            raise ValueError("Can't read frame")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #converting into gray-scale
        cv2.imwrite(name, gray)
        cv2.imshow(temp, gray)
        cv2.waitKey(1)
        
        time.sleep(2)