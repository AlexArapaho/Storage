import math


class Pair:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def mult(self, a, b):
        return self._a * self._b

    def add(self, a, b):
        return self._a + self._b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, a):
        self._a = a

    @b.setter
    def b(self, b):
        self._b = b


class RightTriangle(Pair):

    def __init__(self, a, b,):
        super().__init__(a, b)

    def hypot(self):
        return round(math.sqrt(self._a**2 + self._b**2), 2)

    def area(self):
        return (self.mult(self._a, self._b))/2

    def print_info(self):
        print("Прямоугольный треугольник ", (self._a, self._b, self.hypot()))


p1 = RightTriangle(5, 8)
print("Гипотенуза ", p1.hypot())
print("Площадь ", p1.area())
p1.print_info()
print("Произведение", p1.mult(5, 8))
print("Сумма", p1.add(5, 8))
p1.a = 10
p1.b = 20
print("Гипотенуза ", p1.hypot())
print("Площадь ", p1.area())
p1.print_info()
print("Произведение", p1.mult(5, 8))
print("Сумма", p1.add(5, 8))




