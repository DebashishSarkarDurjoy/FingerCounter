import cv2
import time
import os

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
overLayList = []
for im in myList:
    image = cv2.imread(f'{folderPath}/{im}')
    overLayList.append(image)

pTime = 0
while True:
    success, img = cap.read()

    h, w, c = overLayList[0].shape
    img[0:h, 0:w] = overLayList[0]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = time.time()

    cv2.putText(img, f'FPS: {int(fps)}', (580, 10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
