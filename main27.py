class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y, self.z * other.z

    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y, self.z / other.z

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой!")
        elif item == "x":
            return f"x={self.x}"
        elif item == "y":
            return f"y={self.y}"
        elif item == "z":
            return f"z={self.z}"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой!")
        elif key == "x":
            self.x = value
        elif key == "y":
            self.y = value


p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)
p3 = p1 + p2
p4 = p1 - p2
p5 = p1 * p2
p6 = p1 / p2

print("Координаты первой точки: ", p1)
print("Координаты первой точки: ", p2)
print("Сложение координат: ", p3)
print("Вычитание координат: ", p4)
print("Умножение: ", p5)
print("Деление: ", p6)
print("Равенство координат: ", p1 == p2)
print(p1["x"], p2["x"])
print(p1["y"], p2["y"])
print(p1["z"], p2["z"])
p1["x"] = 20
print("Запись значения в координату x: ", p1["x"])





