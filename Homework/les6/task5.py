'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    title = ""
    def __init__(self, name):
        self.title = name
    def draw(self):
        print("Отрисовка")

class Pen(Stationery):
    def __init__(self):
        print("Pen created")
        super().__init__("Pen")
    def draw(self):
        super().draw()
        print("Sssccrrrr")

class Pencil(Stationery):
    def __init__(self):
        print("Pencil created")
        super().__init__("Pencil")
    def draw(self):
        super().draw()
        print("HHhhhrrrr")
class Handle(Stationery):
    def __init__(self):
        print("Handle created")
        super().__init__("Handle")
    def draw(self):
        super().draw()
        print("Sssshhhhhh")

pen1 = Pen()
pen1.draw()

penc1 = Pencil()
penc1.draw()

h1 = Handle()
h1.draw()