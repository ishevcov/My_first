'''
Декораторы и @wraps

Декоратор это функция обертка, которая оборачивает другую функцию в свой функционал
без изменения основной функции
@decorator  - синтаксис применения

@wraps необходим для передачи значений из документации основной функции в help()
при использовании декораторов

'''

def tagMarker(func):
    def wrapper(*args, **kwargs):
        print("<div>")
        func(*args, **kwargs)
        print('</div>')
    return wrapper

@tagMarker
def printText(text):
    print(text)

printText("Hello world")

import time
import datetime

def recTime(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        done = datetime.datetime.now()-start
        print(f'Функция завершена за {done} секунд')
    return wrapper


@recTime
def sfunc():
    time.sleep(3)
    print("Завершено")

sfunc()

#декораторы позволяют определять время на вычисления и находить оптимальные
#алгоритмы для расчета

