# Игра "Черепашьи гонки". При запуске игры отрисовывается разметка беговой дорожки и
# появляются две черепашки. Скорость каждой участницы задается случайным образом.
# Цель игры угадать, кто прибежит первым.

from turtle import *
from random import randint
from time import *

finish = 200        # дистанция гонки

t1=Turtle()         # Имя первой черепашки(создаем объект класса Turtle()),
                    # в этом момент создается конструктор

t1.shape("turtle")  # Меняем форму черепашки, обращаемся к свойству форма и присваиваем
# форму черепашки
t1.color("red")     # Изменяем цвет черепашки
# Это не работает, разобраться как сделать
# t1.color(randint(0,255), randint(0,255), randint(0,255)) # задать случайный цвет черепашке
t1.penup()          # Поднимаем черепашку, чтобы не рисовала (как перо) 
t1.goto (-200,20)   # Перемещаем черепашку по координатам
t1.pendown ()       # Опустили черепашку, дали возможность рисовать
t1.speed(3)

t2=Turtle()         
t2.shape("turtle")  
t2.color("blue")    
t2.penup()          
t2.goto (-200,-20)  
t2.pendown ()        
t2.speed(3)

def razmetka():     # Функция разметки поля
    t=Turtle()
    t.speed(0)
    for i in range (1,21):
        t.penup()
        t.goto(-200+i*20, 50)
        t.pendown()
        t.goto(-200+i*20, -100)
    t.hideturtle()   

razmetka()

# Функция обработчик события
def catch1(x,y):       # x,y - это текущие координаты
  t1.write('Ouch!', font=('Arial', 14, 'normal'))   # Пишем на экране Ouch  
  t1.fd(randint(10,15)) # Черепашка делает случайный шаг от 10 до 15      

t1.onclick(catch1) # здесь прикркпляем обработчик к событию нажатия на 1 черепашку   

def catch2(x, y):   
  t2.write('Мне больно!',  font=('Arial', 14, 'normal'))    
  t2.fd(randint(10,15))      

t2.onclick(catch2)     

# Пока координата по x первой черепашки меньше finish и 
# координата по x второй черепашки меньше finish делаем:
# Координата по x finish = 200 + 200 = 400
while t1.xcor()<finish and t2.xcor()<finish:
    t1.forward(randint(2,7))  # t1.forward рисует вперед со случайным шагом от 2 до 7    
    t2.forward(randint(2,7))
    sleep(0.05)
    


