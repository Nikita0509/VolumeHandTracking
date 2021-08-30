import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
    results = hands.process(imgRGB)

    print(results)

    


    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    cv.imshow('image', img)
    cv.waitKey(20)