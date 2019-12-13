import datetime

import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_recognition.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX
id = 0

names = ['None', 'Alex_Belan','Bill_Gates', 'Victoria']

cam = cv2.VideoCapture(1)
cam.set(3, 640)
cam.set(4, 480)

PADDING = 20
identities = []
while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        x1 = x - PADDING
        y1 = y - PADDING
        x2 = x + w + PADDING
        y2 = y + h + PADDING
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y1:y2, x1:x2])
        print(confidence)
        if (confidence < 100) and round(100 - confidence) > 50:
            person = names[id]
            identities.append(person)
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            person = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        img = cv2.putText(img, person + '' + confidence, (x1 + 5, y2 - 5), font, 1.0, (255, 255, 0), 2)
        #cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        #cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    if identities != []:
        basename = ""
        for i in identities:
            basename += str(i) + '_'
        identities.clear()
        suffix = datetime.datetime.now().strftime("%H_%M_%S_%d_%m_%Y")
        filename = "".join([basename, suffix])
        path = os.getcwd() + '\photo\ '.replace(' ', '') + filename + '.jpg'
        cv2.imwrite(path, img)
    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # 'ESC' для Выхода
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()