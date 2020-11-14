import cv2
import numpy as np

pts1 = np.float32([])

kernel = np.ones((5, 5), np.uint8)
# img = cv2.imread("./1.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture('./2.MP4')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
while cap.isOpened():
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    imgCanny = cv2.Canny(img, 150, 200)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
    cv2.imshow('img', img)
    cv2.imshow('imgGray', imgGray)
    cv2.imshow('imgBlur', imgBlur)
    cv2.imshow('imgCanny', imgCanny)
    cv2.imshow('imgDilation', imgDilation)
    cv2.imshow('imgEroded', imgEroded)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break