import os

import cv2

cam = cv2.VideoCapture(1)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('Введите id пользователя: ')
print("Смотрите в камеру")
count = 0
PADDING = 20
while (True):
    ret, img = cam.read()
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

    cv2.imshow('photo', img)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 10:
        break

cam.release()
cv2.destroyAllWindows()
