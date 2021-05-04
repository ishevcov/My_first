'''
Наследование и полиморфизм

1.Наследование: принимающий класс потомки, передающий класс родитель
2. Пробрасываем нужные в дочерние классы атрибуты родителя конструкцией
 def __init__(self, atr):
    super().__init__(atr)
    далее прописываем атрибуты потомка
3. можно переопределять методы родителя, просто переписав метод в потомке
под новые нужды
4. Можно выносить логически связнанные атрибуты в отдельный класс и использовать
экземпляры данного класса как атрибуты другого класса

'''


class CarsClass():
    '''Класс автомобилей'''
    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = int(probeg)

    def showCar(self):
        '''Показать информацию о машине'''
        print(f'\nМарка автомобиля-{self.brand}'
              f'\nМодель автомобиля-{self.model}'
              f'\nГод выпуска - {self.year}'
              f'\nПробег - {self.probeg} т. км')
    def drowCar(self, km):
        '''Метод поездки авто'''
        self.probeg = self.probeg + km

#создадим новый класс электромобилей, который включает класс автомобилей

class ClassBattery():
    def __init__(self, battery = 100):
        self.battery = battery

    def descriptionBattery(self):
        '''Выводит информацию о батарее'''
        print('Этот автомобиль имеет заряд батареи: ' + str(self.battery)+' %')


class ElectroCar(CarsClass):
    '''Класс элктрокаров, инициализация атрибутов'''
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = ClassBattery()





s_car = CarsClass('Лада', 'Калина', '2009', '140')
s_car.showCar()
s_car.drowCar(100)
s_car.showCar()

tesla = ElectroCar('Tesla', 'T', '2017', '140')
tesla.showCar()
tesla.battery.battery = 80
tesla.battery.descriptionBattery()




