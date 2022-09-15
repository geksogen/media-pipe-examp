#   cannot import name '_registerMatType' from 'cv2.cv2'
#   https://stackoverflow.com/questions/70537488/cannot-import-name-registermattype-from-cv2-cv2
#   https://github.com/cvzone/cvzone


import cv2
from cvzone.HandTrackingModule import HandDetector

print(cv2.__version__)
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,200)
cap.open(0, cv2.CAP_DSHOW)
cap.set(10,150)

height = 200

detector = HandDetector(maxHands=1, detectionCon=0.8)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    data = []

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        print(lmList)
        for lm in lmList:
            data.extend([lm[0], height - lm[1], lm[2]])
        print(data)


    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()