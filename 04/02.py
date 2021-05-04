'''
1.Класс - шаблон создания обьектов, обеспечивающий начальные значения
состояний, значения атрибутов и методов
2.self - ссылка на обьект класса
3. Метод - функция которая может  быть применена к обьекту класса
4. Обращаемся к атрибутам обьекта класса используя точечную запись
обьект.атрибут
5. Применяем метод к обьектам, используя обращение через точку
обьект.метод()
6. Передаем дополнительные атрибуты метода, как в функциях, именованными
или неименованными параметрами
обьект.метод(атрибут1 = параметр)

'''

class CommentFromWebSite():
    '''Комментарии с сайта'''
    def __init__(self, data, text, likes):
        self.data = data
        self.text = text
        self.likes = int(likes)

    def showComent(self):
        '''Вывести комментарий в терминал'''
        print(f'\nКомментарий с сайта, \nДата: {self.data}',
        f'\nТекст: {self.text}, лайков {self.likes} ')

    def changeLikes(self):
        '''Прибавляет лайк при запросе'''
        self.likes = self.likes + 1

    def changeComent(self, new_text):
        '''Изменение комментария'''
        self.text = new_text


new_comment = CommentFromWebSite('11/02/2020', 'Первый', '11')
print(type(new_comment))
print(new_comment.text)
new_comment.text = 'Новый коммент!'
print(new_comment.text)

new_comment2 = CommentFromWebSite('22/03/19', 'Второй', '5')
new_comment2.showComent()
new_comment2.changeLikes()
new_comment2.showComent()
new_comment2.changeComent('Новый комментарий')
new_comment2.showComent()




