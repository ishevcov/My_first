'''
Тип set  - последовательность уникальных обьектов
синтаксис : s = {element, element,  }
add - добавление элемента к множеству
remove  - удаляет элемент по имени
union - обьединяет два множества
intersection  - функция пересечение, выдает элементы которое есть
в первом и во втором списке
difference - функция вычитания, выдает элементы которые есть в первом, исключая
те которые есть во втором списке
issubset - является ли первое множество подмножеством второго
set не поддерживает обращение по индексу
'''

first_set = {'Alex', 'John', 'Georg', 'Alex'}
print(type(first_set))
print(first_set)
print(len(first_set))

first_set.add('Max')

print(len(first_set))
print('Max' in first_set)
first_set.remove('Alex')
print(first_set)

first_set_1 =  {'Alex', 'John', 'Georg', 'Alex'}
second_set_1 = {'Anton', 'Tom', 'Anna', 'Alex'}
third_set = first_set_1.union(second_set_1)
print(third_set)
fourth_set = first_set_1.intersection(second_set_1)
print(fourth_set)
five_set = first_set_1.difference(second_set_1)
print(five_set)
print(first_set_1-second_set_1)

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))
print(set2.issuperset(set2))