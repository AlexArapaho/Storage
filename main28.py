class Descr:
    def __set_name__(self, owner, name):
       self.name = name

    def __get__(self, instance, value):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not (value > 0 and isinstance(value, int)):
            raise ValueError(f"{self.name} должно быть положительным целым числом")
        instance.__dict__[self.name] = value


class Triangle:
    a = Descr()
    b = Descr()
    c = Descr()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def exist(self):
        if (self.a + self.b) > self.c and (self.a + self.c) > self.b and (self.b + self.c) > self.a:
            print(f"Треугольник со сторонами {self.a}, {self.b}, {self.c} существует")
        else:
            print(f"Треугольник со сторонами {self.a}, {self.b}, {self.c} не существует")


p1 = Triangle(2, 5, 6)
p1.exist()
p1 = Triangle(5, 2, 8)
p1.exist()
p1 = Triangle(7, 3, 6)
p1.exist()

