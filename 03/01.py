'''
Функции def
Необходимы для минимизации повторяющейся части кода
'''

def printText():
    print("Hello world")

def printText_1(msg, end = "!"):
    print(msg+end)

def sqRing(p):
    return 3.1415*(p**2)

def getSquare(w, h):
    '''
    :param w: Компонент
    :param h: Компонент
    '''
    return 2*(w+h), w*h

a = False
if a:
    def sFunc(x,y,z):
        return x+y+z
else:
    def sFunc(a,b,c):
        x = a+b/c
        return x



print(type(getSquare(5,5)))

print(sqRing(10))

printText()
printText_1("Hello")
printText_1("Hello", "^")
printText_1("Hello", end="@")

print(sFunc(10, 20, 30))

help(getSquare)
