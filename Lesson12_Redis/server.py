from tkinter import DISABLED
import redis
import random

# Открываем соединение и кладем его в переменную redis_server
# Конструкция with позволяет автоматом закрыть файл после окончания с ним работы
with redis.Redis() as redis_server:
    # Кладем значения в очередь слева lpush -> Leftpush
    redis_server.lpush("queue", random.randint(0, 10))
    
# После запуска программы в терминале сервера пишем команду 
# LRANGE queue 0 -1, -1 означает до конца
# проверив  вставилось ли наше значение