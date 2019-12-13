import os

import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    face = []
    ids = []

    for imagePath in imagePaths:
        img = cv2.imread(imagePath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face.append(img)
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        ids.append(id)
    return face, ids


rec = int(input("Введите 1 для обучения на фото с веб-камеры, 2 для обучения на простых фотографиях: "))
path = ' '
path1 = ' '
if rec == 1:
    path = os.getcwd() + '\\person_from_web_camera\\'
    path1 = os.getcwd() + '\\face_recognition\\face_recognition_web_camera.yml'
elif rec == 2:
    path = os.getcwd() + '\\person_from_photo\\'
    path1 = os.getcwd() + '\\face_recognition\\face_recognition_photo.yml'
else:
    print("Ошибка выбора варианта для обучения!")
faces, ids = getImagesAndLabels(path)

recognizer.train(faces, np.array(ids))

recognizer.write(path1)
