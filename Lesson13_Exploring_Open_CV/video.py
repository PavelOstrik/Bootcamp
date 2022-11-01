# Установить библиотеку OpenCV
# pip install opencv-python 
# Подключаем установленную библиотеку
import cv2

# Объявляем переменную  в которую загружаем наш классификатор, обращаясь к библиотеке cv2
# Проходим по пути классификатора и через + вставляем нужный нам
# cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# Мы будем работать с лицами
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# # Считываем лицо с простой картинки
# img = cv2.imread('face.jpg') # Метод чтения изображения
# # Конвертируем наше изображенеие в серый увет, так как распознавать объекты
# # легче всего на сером оттенке с помощью метода cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Обращаемся к нашему классификатору face_cascades и обращаемся к методу
# # detectMultiScale(img_gray) он находит те координаты в которых мы будем преполагать
# # что там находятся лица
# faces = face_cascades.detectMultiScale(img_gray)
# # print(faces)
# # [[ 47 109 178 178]] 
# # 47 109 координаты начала нашего прямоугольника
# # 178 178 длина и ширина

# # Теперь наложим наш прямоугольник на наше изображение
# # cv2.rectangle рисования простого, объемного или заполненного вертикального прямоугольника
# # (x, y) вершина
# # (x + w, y + h) размер
# # (255, 0, 0) цвет линии, 2 толщина линии
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


# cv2.imshow('Result', img)
# cv2.waitKey(0)

# Создаем переменную для работы с видео, (0) означает что вебкамера одна
# Если вебкамеры нет то можно скачать видео и казать его путь взмен номера камеры
# cap = cv2.VideoCapture("   ")
cap = cv2.VideoCapture(0)

# Так как мы не знаем когда остановится видео пишем бесконечный цикл
while True:
    # Мы должны постоянно считывать кадр
    # При вызове метода cap.read() в переменную frame записывается картинка
    # success, frame булевая переменная, которая говорит удлось получить кадр или нет
    # _, 
    _, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    # cv2.imshow('Preview', frame)  
    faces = face_cascades.detectMultiScale(img_gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Выводим на экран нашу картинку
    cv2.imshow('Result', frame)

    # Пишем, чтобы окно с картинкой не закрывалось сразу, 
    # кадр будет обновлятся с задержкой в 1 милисикунду
    # Эта строка позволит нам выйти из бесконечного цикла когда мы нажмем на 'q'
    # Если работаем не с вебкамерой, а с видео waitKey(1 / 1000) чтобы была плавность
    # картинки
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
    # Посмотреть результат стоп кадра до наложения прямоуголтника и после:
    # Меняем 1 на 0 чтобы было вечное ожидание
    # И вставляем еще один вывод картинки cv2.imshow('Preview', frame)
    # if cv2.waitKey(0) & 0xff == ord('q'):
    #     break