'''
map file and lambda functions

1) Функция map применяет другую функию к каждому элементу последовательности
2) Функция filter применяет другую функцию проверки с результатом типа bool
к каждому элементу последовательности отфильтровывая значение с Thru
3) lambda  - анонимная функция без обьявления, служит для сокращения записи
простых функция, злоупотреблять не стоит

'''

#что такое map
'''
def map(func, iterable):
    for i in iterable:
        yield func(i)
'''

def sq(x):
    return x**2

a= [-2, -1, 5]
b = map(sq, a)
c = list(b)
print(b)
print(c)

d = ["hello", "absc", "good"]
e = list(map(str.upper, d))
print(d)
print(e)


age = [11, 20, 18, 33, 12]

#ниже приводится две идентичные функции, которые записаны разными способами
#использование лямбда функций приводит к снижению читаемости кода
def is_adult(age):
    return age>=18

is_adalt = lambda age: age>=18

f = filter(is_adult, age)
f1 = filter(is_adalt, age)
print(list(f))
print(list(f1))




