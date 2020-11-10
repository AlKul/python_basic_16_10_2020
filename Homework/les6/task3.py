'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
    name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.position = "Somebody"
        #self._income = {"wage": wage, "bonus":bonus}
        #self._income = {"wage": 0, "bonus": 0}
        self._income = {}
        print("Worker")


class Position(Worker):

    def __init__(self, position, name, surname, wage, bonus):
        self.position = position
        #self.name, self.surname = name, surname
        super().__init__(name, surname)
        self._income["wage"] = wage
        self._income["bonus"] = bonus
        print("Position")

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return(self._income["wage"] + self._income["bonus"])




w1 = Position("Analyst", "John", "Johnoff", 30000, 10000)