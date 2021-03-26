'''
Словарь, тип dict(dictionary). Тип данных существующий в виде пар ключ-значение

Синтаксис dict: dict = {'ключ': Значение, 'ключ': Значение }
Все ключи уникальны, повторений быть не может
Обновление и добавление осуществляется с помощью присвоения
dict[key]=new_data
Функция get выдает значение по ключу
Функция setdefault добавляет пару, где ключ берется из аттрибута функции,
а значение выставляется none
Функция pop удаляет пару из словаря по ключу
Функция keys выдает все ключи словаря
Функция values выдает все значения словаря

'''

dict_1 = {

    "mark": 5,
    "tom": 10
}

print(dict_1)
print(dict_1.get('tom'))
dict_1['man'] = 13
print(dict_1)
dict_1.setdefault('oleg')
print(dict_1)
dict_1.pop('oleg')
print(dict_1)
print(dict_1.keys())
key_list = list(dict_1.keys())
print(key_list)
print(dict_1.values())
print(type(dict_1.values()))
print("anna" in dict_1)
