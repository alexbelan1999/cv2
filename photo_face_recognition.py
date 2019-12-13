import datetime
import glob
import os

import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
rec = int(input("Введите 1 для фото с веб-камеры, 2 для простых фотографиях: "))
names = None
if rec == 1:
    recognizer.read(os.getcwd() + '\\face_recognition\\face_recognition_web_camera.yml')
    names = ['None', 'Alex_Belan', 'Vitaly_Belan']
elif rec == 2:
    recognizer.read(os.getcwd() + '\\face_recognition\\face_recognition_photo.yml')
    names = ['None', 'Bill_Gates', 'Elon_Musk', 'Steve_Jobs']
else:
    print("Ошибка выбора варианта!")
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX
id = 0

PADDING = 20
identities = []
str1 = "testphoto/*"

for file in glob.glob(str1):
    identity = os.path.splitext(os.path.basename(file))[0]
    img = cv2.imread(os.getcwd() + '\\testphoto\\' + identity + '.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    faces_detected = "Лиц обнаружено: " + format(len(faces))
    print(faces_detected)

    for (x, y, w, h) in faces:
        x1 = x - PADDING
        y1 = y - PADDING
        x2 = x + w + PADDING
        y2 = y + h + PADDING
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        print(confidence)
        if (confidence < 100):
            person = names[id]
            identities.append(person)
            confidence = "  {0}%".format(round(100 - confidence))

        else:
            person = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        img = cv2.putText(img, person + '' + confidence, (x1 + 5, y2 - 5), font, 1.0, (255, 255, 0), 2)
        cv2.imshow('camera' + person + str(confidence), img)

    if identities != []:
        basename = ""
        for i in identities:
            basename += str(i) + '_'
        identities.clear()
        suffix = datetime.datetime.now().strftime("%H_%M_%S_%d_%m_%Y")
        filename = "".join([basename, suffix])
        path = os.getcwd() + '\photo\ '.replace(' ', '') + filename + '.jpg'
        cv2.imwrite(path, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
