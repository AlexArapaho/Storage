class Clock:
    DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        elif other.sec == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        elif other.sec == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec == other.sec

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec >= other.sec

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec < other.sec


    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec <= other.sec



c1 = Clock(600)
c2 = Clock(200)
c3 = c1 - c2
# c1 -= c2
c4 = c1 * c2
# c1 *= c2
c5 = c1 // c2
# c1 //= c2
c6 = c1 % c2
# c1 %= c2


print("c1: ", c1.get_format_time())
print("c2: ", c2.get_format_time())
print("c1 - c2: ", c3.get_format_time())
print("c1 * c2: ", c4.get_format_time())
print("c1 // c2: ", c5.get_format_time())
print("c1 % c2: ", c6.get_format_time())
print("c1 > c2: ", c1 > c2)
print("c1 >= c2: ", c1 >= c2)
print("c1 < c2: ", c1 < c2)
print("c1 <= c2: ", c1 <= c2)

