import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Alexface.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
# Тип шрифта
font = cv2.FONT_HERSHEY_SIMPLEX

# iniciate id counter
id = 0

# Список имен для id
names = ['None', 'Alex_Belan','Bill_Gates', 'Victoria']

cam = cv2.VideoCapture(1)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height
PADDING = 30
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10),
    )

    for (x, y, w, h) in faces:
        x1 = x - PADDING
        y1 = y - PADDING
        x2 = x + w + PADDING
        y2 = y + h + PADDING
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Проверяем что лицо распознано
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # 'ESC' для Выхода
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()