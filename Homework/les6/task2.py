'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
    толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:
    _length = 0.
    _width = 0.
    _mass_per_m_sq = 25.
    _mass = 0.

    def __init__(self, length, width):
        '''
        :param length: m
        :param width: m
        '''
        self._length = length
        self._width = width
        print("Road created: ", length, "   ", width, sep = "--")

    def mass(self):
        self._mass = self._length * self._width *  self._mass_per_m_sq
        return self._mass

r1 = Road(132, 1231)
print(r1.mass()/1000, "tons")