import os

import psycopg2

exit = True
connection = None

try:
    print("Скачивание данных с сервер.")
    n = int(input("Введите 1 для скачивание данных для веб-камеры, 2 для скачивание данных для фотографий: "))
    sql = " "
    if n == 1:
        sql = "SELECT lo_export(object,'" + os.getcwd() + r"\face_recognition\face_recognition_web_camera1.yml') from datacv2 where name = 'web_camera_data';"

    elif n == 2:
        sql = "SELECT lo_export(object,'" + os.getcwd() + r"\face_recognition\face_recognition_photo1.yml') from datacv2 where name = 'photo_data';"

    else:
        print("Ошибка выбора варианта!")

    connection = psycopg2.connect(dbname='cv2', user='postgres', password='1234', host='127.0.0.1')
    with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
        cursor.close()


except psycopg2.OperationalError:
    print("Ошибка соединения с базой данных!")
    exit = False

finally:
    if exit == True:
        connection.close()
        print("Скачивание файлов с сервера завершено. Соединение закрыто")
