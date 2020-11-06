import cv2
import os
import time
import numpy as np
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0
path='D:/datatrain'
dim=(640,480)
name=input('Your name: ')
path1=os.path.join(path,name)
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
createFolder(path1)

while True:
    time.sleep(0.5)
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(path1,str(name)+str(img_counter)+'.png'),frame)
    img_counter+=1
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
cam.release()

cv2.destroyAllWindows()
