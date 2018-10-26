# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import sys
import math


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        try:
            self.x1 = int(x1)
            self.y1 = int(y1)
            self.x2 = int(x2)
            self.y2 = int(y2)
            self.x3 = int(x3)
            self.y3 = int(y3)
        except ValueError:
            print("Ошибка. Введите координаты в виде чисел.")
            sys.exit()
        self.ab = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.ac = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        self.bc = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)

    # Square - Площадь
    def square(self):
        sq = 0.5 * abs((self.x1 - self.x3) * (self.y2 - self.y3) - (self.x2 - self.x3) * (self.y1 - self.y3))
        return sq

    # Heigh - Высота
    def heigh(self):
        return 2 * self.square() / self.ac

    # Perimeter - Периметр
    def perimeter(self):
        return self.ab + self.ac + self.bc

    def param(self, name):
        print('Параметры треугольника № {}:'.format(name))
        print('Площадь  =', self.square())
        print('Периметр =', self.perimeter())
        print('Высота =', self.heigh())


triangle1 = Triangle(1, 1, 6, 7, 8, 4)
triangle2 = Triangle(-2, -2, -4, -5, -6, -3)
triangle3 = Triangle(0, 0, 8, 2, -2, 6)

triangle1.param(1)
triangle2.param(2)
triangle3.param(3)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

