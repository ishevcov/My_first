'''
1. магические (Dunder) методы __str__ и __rerp__ служат для строкового
представления обьекта
2. Метод возвращает строковое представление заданного атрибута класса
3. Конструкция
    def __str__(self):
        return self.atr
4. Чаще всего используют метод Str, и в Django мы будем работать именно с ним


'''

class New():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

new_obj = New('Ivan')
print(new_obj)


