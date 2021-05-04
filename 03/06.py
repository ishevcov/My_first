'''
Ошибки и исключения

Применяем конструкцию try except finally

try - тело программы, то что выполняется
except - действия при возникновении ошибки
finally - действие которое выполнится всегда
'''

'''

while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a/b)
    #except ValueError:
    #    print('Ошибка! Введите число, а не текст')
    #except ZeroDivisionError:
    #    print('Ошибка! Делить на ноль нельзя')
    except Exception as e:
        print(e, type(e))
    finally:
        print('Операция завершена')
'''



import requests

try:
    a = requests.get('https://45yandex.ru/re')
    print(a)
except requests.exceptions.ConnectionError:
    print('Сервер упал!')
