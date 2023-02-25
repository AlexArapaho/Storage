import math


class Sphere:

    def __init__(self, radius,  x, y, z):
        self.__radius = self.__x = self.__y = self.__z = 0
        if Sphere.__check_value(radius) and Sphere.__check_value(x) and Sphere.__check_value(y) and Sphere.__check_value(z):
            self.__radius = radius
            self.__x = x
            self.__y = y
            self.__z = z

    def __check_value(arg):
        if isinstance(arg, int) or isinstance(arg, float):
            return True
        return False

    def set_radius(self, radius):
        if Sphere.__check_value(radius):
            self.__radius = radius
        else:
            print("Некоректый тип данных")

    def set_center(self, x, y, z):
        if Sphere.__check_value(x) and Sphere.__check_value(y) and Sphere.__check_value(z):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            print("Некоректый тип данных")

    def get_radius(self):
        return self.__radius

    def get_volume(self):
        return (math.pi*self.__radius**3)*(4/3)

    def get_square(self):
        return 4*math.pi*self.__radius**2

    def get_center(self):
        return (self.__x, self.__y, self.__z)

    def is_point_inside(self, x, y, z):
        if math.sqrt(x**2 + y**2 + z**2) < self.__radius:
            return True
        else:
            return False


ex = Sphere(0.6, 1, 2, 3)
ex.set_center(0, 0, 0)
print("Радиус сферы: ", ex.get_radius())
print("Объём сферы: ", ex.get_volume())
print("Площадь поверхности: ", ex.get_square())
print("Координаты центра сферы: ", ex.get_center())
print("Точка внутри сферы: ", ex.is_point_inside(0, -1.5, 0))
ex.set_radius(1.6)
print("Новый радиус: ", ex.get_radius())
print("Точка внутри сферы: ", ex.is_point_inside(0, -1.5, 0))


