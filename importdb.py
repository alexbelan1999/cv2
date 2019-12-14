import os

import psycopg2

exit = True
connection = None

try:
    print("Загрузка данных на сервер.")
    n = int(input("Введите 1 для загрузки данных с веб-камеры, 2 для загрузки данных с фотографий: "))
    sql = " "
    if n == 1:
        sql = "INSERT INTO public.datacv2 (name, object) VALUES ('web_camera_data', lo_import('" + os.getcwd() + r'\face_recognition\face_recognition_web_camera.yml' + "'));"

    elif n == 2:
        sql = "INSERT INTO public.datacv2 (name, object) VALUES ('photo_data', lo_import('" + os.getcwd() + r'\face_recognition\face_recognition_photo.yml' + "'));"

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
        print("Отправка файлов на сервер завершена. Соединение закрыто")
