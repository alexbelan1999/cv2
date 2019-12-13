import glob
import os
import cv2
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('\n enter user id end press  ==>  ')

str1 = "images/Bill_Gates/*"
count = 0
for file in glob.glob(str1):
        identity = os.path.splitext(os.path.basename(file))[0]
        image = cv2.imread(os.getcwd() + '\\images\\Bill_Gates\\'+identity+ '.jpg')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                count += 1
                # Сохраняем лицо
                path = os.getcwd() + '\\person\\user.' + str(face_id) + '.' + str(count) + '.jpg'
                cv2.imwrite(path, gray[y:y + h, x:x + w])
        cv2.imshow('image', image)


