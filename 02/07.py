'''
цикл while условно бесконечный цикл пока выполняется условает Thru
0) continue/break/pass работает как в for так и в while
1) continue переход к следующему действию
2) break останавливает цикл
3) pass ничего, никакого действия
'''

import time

x=1
'''
while True:
    x = x+x
    print(x)
    time.sleep(1)
'''
'''
while x<6:
    print(f'X равно {x}')
    x +=1
    time.sleep(0.5)
else:
    print('Завершено')
'''
vals = [1, 2, 3, 4, 5, 6,7,  8, 8, 9, 95, 6]
summa = 0
for x in vals:
    if x%2 ==0:
        continue
    else:
        summa += x
    if summa > 10:
       break
print(summa)

