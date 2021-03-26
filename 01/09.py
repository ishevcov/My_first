'''
Варианты форматирования строк
Переменные x=1, y=2
1. строка = ('{} текст {}'.format(x,y))
2. строка с позиционированием переменных  = ('{0} текст {1}'. format(x,y))
3. сокращенный формат строка = (f'{x} текст {y}' )

'''

x = '10'
y = 'cold'
print('Weather: temperature +{} and it\'s {}'.format(x, y))
print('Weather: temperature +{1} and it\'s {0}'. format(x,y))
print(f'Weather: temperature +{x} and it\'s {y}')

