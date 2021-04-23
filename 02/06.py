"""
#For циклично повторяющиеся операции
1) Функция range() создает диапазон
2) enumerate() добавляет счетчик каждому обьекту, исп для построения
индекса
3)для чтения словаря используем функцию items()
4)Для чтения значений словаря используем values()

"""


numbers  = [1, 2, 3, 4, 5]
new_list  = []

for i in numbers:
    new_list.append(i)

print(new_list)

for x, item in enumerate(numbers):
    numbers[x] +=10
print(numbers)

for _ in range(1, 5):
    print("Ошибка!")

some_tuple = (11, "Alex", 3.01)
for x in some_tuple:
    print(x)

#хитрая комбинация list и tuple
some_list = [("John", 22), ("Alex", 23)]

for  (name, age) in some_list:
    print(f'{name} is {age} year old')

some_dict = {
    "Alex": 11,
    "Maxim":222,
    "Oleg": 23
}

for x in some_dict:
    print(x)
for x in some_dict.items():
    print(x)
for x, y in some_dict.items():
    print(f'Ключ {x} и значение {y}')
for value in some_dict.values():
    print(value)










