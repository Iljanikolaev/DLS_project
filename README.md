# DLS_project
Проект для Deep Learning School(DLS)

1)Я решил реализовать веб-приложение, сайт, куда можно загрузить изображение и получить результат детекции(изображение с Bounding-Boxes и списком распознанных объектов).
Выбран детектор yolov5 - одностадийный детектор, разработанный компанией ultralytics, реализованный на фреймворке pytorch и обученный на датасете COCO(80 классов). 

2)Детектор был запущен на случайных изображениях. Результат вы сможете увидеть открыв файл Yolov5Examples.ipynb в Google Colab 
или на сайте http://iljanikolaev.ru/admin/ => Detection => Записи(чтобы открыть полноразрмерное изображение: правая кнопка мыши и открыть изображение в новой вкладке).

3)Для разработки бэкенда был выбран фреймворк django, так как он написан на python.

4)Разработка демо

Принцип работы:

1.Пользователь загружает картинку на сервер

2.Сервер подает полученное изображение на вход детектора

3.Сервер демонстрирует на веб-странице пользователю результат детекции

Так как хостинг серверов с gpu достаточно дорогой, этот проект(сайт и нейронная сеть) 
полностью работают на цпу, что увеличивает время анализа каждого изображения.
Чтобы время обработки было не слишком большим используется модель yolov5s(c минимальным количеством параметров).

5)Сеть в сайт была встроена следующим образом:
Пользователь отправляет изображение на сервер=>Сервер сохраняет картинку в базу данных(Input)=>Сервер запускает детектор и передает сохраненное изображение на вход детектора
=>yolov5s анализирует изображение=>yolov5s выдает результат детекции=>Картинка с Bounding-Boxes и список распознанных объектов сохраняется во второй базе данных(Detection)
=>Сервер выводит на веб-страницу результат детекции из второй базы данных(Detection)
На сервере две модели Django(БД-MySQL): одна для сохранения входных изображений, вторая для сохранения результатов детекции(изображение с Bounding-Boxes и списком распознанных объектов).
В процессе нужно было отредактировать файлы yolov5.

6)Тестирование отдельных функций и модулей производитлось в течение разработки проекта.
Также были проведены user-тесты.

7)Демо оформлено для показа другим людям. Сайт выложен на хостинг и доступен по домену: http://iljanikolaev.ru/input/
На сайт можно загрузить любое изображение и, нажать кнопку "отправить", получить результат детекции.
Также можно зайти в админку сайти login - iljanikolaev, password - supersecret. В админке можно увидеть записи для БД для входных(Input - id, время загрузки, изображение)
 и результирующий изображений(Detection - id, время загрузки, изображение с Bounding-Boxes, список распознанных объектов).

Чтобы запустить локально, нужно создать виртуальное окружение и установить зависимости из requirements.txt.
Далее в папке с проектом выполнить команду: python manage.py runserver. Сайт будет доступен по ссылке: http://127.0.0.1:8000/input/ .

В случае воникновения вопросов, обращайтесь в телеграмме по нику: @Iljanikolaev.
Хостинг сервера оформлен на месяц, так что если вдруг сайт не работает - напишите мне, пожалуйста, я продлю хостинг.
