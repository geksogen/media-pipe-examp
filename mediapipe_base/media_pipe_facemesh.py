#   cannot import name '_registerMatType' from 'cv2.cv2'
#   https://stackoverflow.com/questions/70537488/cannot-import-name-registermattype-from-cv2-cv2
#   https://github.com/cvzone/cvzone

import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

print(cv2.__version__)
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
cap.open(0, cv2.CAP_DSHOW)
cap.set(10,150)
h = 800

detector = FaceMeshDetector(maxFaces=2)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)

    data = []

    if faces:
        print(faces[0])
        #face = faces[0]
        #for lm in faces:
        #    data.extend([lm[0], lm[1], lm[2], lm[3], lm[4], lm[5], lm[6]])
        #print(data)


    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()