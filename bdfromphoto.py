import glob
import os

import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = int(input('Введите id пользователя: '))

path = ''
if face_id == 1:
    path = "images/Bill_Gates/*"

elif face_id == 2:
    path = "images/Elon_Musk/*"

elif face_id == 3:
    path = "images/Steve_Jobs/*"

else:
    print('Ошибка варианта!')

count = 0
PADDING = 20

for file in glob.glob(path):
    identity = os.path.splitext(os.path.basename(file))[0]
    img = None
    if face_id == 1:
        img = cv2.imread(os.getcwd() + '\\images\\Bill_Gates\\' + identity + '.jpg')

    elif face_id == 2:
        img = cv2.imread(os.getcwd() + '\\images\\Elon_Musk\\' + identity + '.jpg')

    elif face_id == 3:
        img = cv2.imread(os.getcwd() + '\\images\\Steve_Jobs\\' + identity + '.jpg')

    else:
        print('Ошибка варианта!')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.2, 5)
    faces_detected = identity + " лиц обнаружено: " + format(len(faces))
    print(faces_detected)

    for (x, y, w, h) in faces:
        x1 = x - PADDING
        y1 = y - PADDING
        x2 = x + w + PADDING
        y2 = y + h + PADDING
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        count += 1
        path = os.getcwd() + '\\person_from_photo\\user.' + str(face_id) + '.' + str(count) + '.jpg'
        cv2.imwrite(path, gray[y1:y2, x1:x2])
        cv2.imshow('photo' + str(count), img)

print("Подготовка фотографий для пользователя ", face_id, " завершена")
cv2.waitKey(0)
cv2.destroyAllWindows()
