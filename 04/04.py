'''
Инкапсуляция: приватные и защищенные атрибуты

1. Публичные атрибуты и методы -доступные к прочтению или вызову за пределами класса
2. Защищенные  - закрытые к прочтению и изменению только на уровне договоренности,
прочитать можно, злоупотреблять не стоит!
3. Приватные  - закрытые к прочтению и изменению на уровне языка (не полностью,
прочитать все же можно) читать нельзя!
4.Вызов приватных методов с помощью публичных:
    def publicmethod(self):
        self.__privatemethod()
    def __privatemethod(self):
obj.publicmethod()

'''

class VkAccountWebSite():
    '''Ваш аккаунт в VK, на сайте ВК'''

    def __init__(self, name, login_id, password):
        self.__name = name
        self.__login_id = login_id
        self.__password = password

    def publicLogin(self):
        self.__loginVk()


    def __loginVk(self):
        if self.__login_id == 123 and self.__password ==456:
            print('Привет '+self.__name)
        return True

vkakk = VkAccountWebSite('Alex', 123, 456)
vkakk.publicLogin()

