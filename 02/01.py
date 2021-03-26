'''
Списки типа list

синтаксис spisok = [element, element,...]
list поддерживает обращение по индексу spisok[0]
list поддерживает срезы spisok[:5]
append - добавляет элемент к списку в конец
insert - вставляет элемент по индексу spisok.insert[7, element].
При этом элемент встанет между элементамии не затрет существующий список
index - возвращает индекс элемента
pop - удаляет последний элемент, а при использовании индекса удаляет по индексу
clear - очистка списка
sort - сортировка списка, поддерживается сортировка по ключу
revers - поворачивает список от последнего к первому
'''

new_list = [1,2,3,4, 'Text']
list_1 = ['alex', 'john']
list_2 = ['mike', 'ruby']
print(type(new_list))
print(len(new_list))
print(new_list[0])
print(list_1+list_2)
list_1.append('anna')
print(list_1)
list_1.insert(1,'ben')
print(list_1)
list_3  = [33, 43, 56, 67]
list_3.sort()
print(list_3)
list_3.sort(reverse=True)
print(list_3)
list_4 = ['a', 'sd', 'fgfg', 'fg']
list_4.sort(key=len)
print(list_4)



