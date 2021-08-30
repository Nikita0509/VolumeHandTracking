import cv2 as cv
import numpy as np
import time
import handTrackingModule as htm


pTime = 0
cTime = 0
cap = cv.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    if len(lmlist) !=0:
        print(lmlist[4])


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img,str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX_SMALL,3,(0,255,0), 3)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    cv.imshow('Image', img)
    cv.waitKey(1)

