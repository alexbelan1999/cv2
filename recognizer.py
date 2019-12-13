import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    face=[]
    ids = []

    for imagePath in imagePaths:
        img = cv2.imread(imagePath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face.append(img)
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        ids.append(id)
    return face,ids

path = os.getcwd() + '\\person\\'
faces,ids = getImagesAndLabels(path)

recognizer.train(faces, np.array(ids))

recognizer.write('face_recognition.yml')