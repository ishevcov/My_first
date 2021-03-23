

'''
Строки
спец символ r для пути r' C_Users
спец символ \n для переноса строки
индекс начинает свой отчет с 0
обращение к элементу по индексу
срез - выбор элементов из последовательности  __с__ по __по__
Конструкция среза :
-от индекса 8 до конца text[8:]
-от начала до индекса 8 text[:8]
-с шагом 1  text[::1]
'''

x = 'Alex'
print(x)
z = "Sone 'long' text"
print(z)

x = "Sone \'long\' text"
print(x)

y=   'C:\\Users\\dell'
y_1=r'C:\Users\dell'
print(y)
print(y_1)

x = 'Some long text \nand new string \nand new string'
print(x)

text = str('hello world')
#конкатинация -сложение символов строки
print(text[0])
print(text[0]+text[1])

#последний элемент массива
print(text[-1])
print(text[2:])
print(text[::1])
print(text[::2])

