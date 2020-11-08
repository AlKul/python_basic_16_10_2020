'''
 Реализуйте базовый класс Car.
 У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
 остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
 Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
from time import sleep as sleep
class Car:
    speed = 0.
    color = ""
    name = ""
    is_police = False
    k = 1

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, ": ")
        print("Speeding up...", end = "")
        sleep(2.5/self.k)
        print("40", end = "...")
        self.speed = 40.
        sleep(2.5/self.k)
        print("60", end = "...")
        self.speed = 60.
        sleep(2.5/self.k)
        print("80")
        self.speed = 80.


    def stop(self):
        print(self.name, ": ")
        print("Stopping!")
        sleep(1)
        print("0")
        self.speed = 0

    def turn(self, direction):
        print(self.name, ": ")
        print("Turning", direction)
    def show_speed(self):
        print(self.name, ": ")
        print("( / )Speed:", self.speed)

class TownCar(Car):
    k = 2
    def __init__(self, color, name):
        self.color = color
        self.name = name
        super().__init__(0, self.color, self.name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Attention! Slow down!")

class Sport_car(Car):
    k = 2.9
    def __init__(self, color, name):
        self.color = color
        self.name = name
        super().__init__(0, self.color, self.name, False)

    def show_speed(self):
        super().show_speed()

class WorkCar(Car):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        super().__init__(0, self.color, self.name, False)
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Attention! Slow down!")

class Police_car(Car):
    k = 2.2
    def __init__(self, color, name):
        self.color = color
        self.name = name
        super().__init__(0, self.color, self.name, True)
    def show_speed(self):
        super().show_speed()


Town1 = TownCar("Grey", "Audi")
Town1.go()
Town1.turn("Left")
Town1.show_speed()


Sport1 = Sport_car("Red", "Ferrari")
Sport1.go()
Sport1.turn("Right")
Sport1.show_speed()


Police = Police_car("Black&White", "Charger")
Police.go()
Police.show_speed()
Sport1.stop()

Town1.show_speed()