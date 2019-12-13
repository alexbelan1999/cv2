import glob
import os
import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('Введите id пользователя: ')

str1 = "images/Bill_Gates/*"
count = 0
PADDING = 20

for file in glob.glob(str1):
        identity = os.path.splitext(os.path.basename(file))[0]
        img = cv2.imread(os.getcwd() + '\\images\\Bill_Gates\\'+identity+ '.jpg')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
                x1 = x - PADDING
                y1 = y - PADDING
                x2 = x + w + PADDING
                y2 = y + h + PADDING
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                count += 1
                path = os.getcwd() + '\\person\\user.' + str(face_id) + '.' + str(count) + '.jpg'
                cv2.imwrite(path, gray[y1:y2, x1:x2])
                cv2.imshow('photo'+str(count), img)

print("Подготовка фотографий для пользователя ",face_id," завершена")
