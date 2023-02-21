class Car:

    def __init__(self, model, year, maker, power, color, price):
        self.model = model
        self.year = year
        self.maker = maker
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print("*" * 10, "Данные автомобиля", "*" * 10)
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.maker}\n"
              f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}\n")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_maker(self, maker):
        self.maker = maker

    def get_maker(self):
        return self.maker

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


bmw = Car("X7 M50i", "2021", "BMW", "530 л.с.", "белый", "10 790 000")
bmw.print_info()
bmw.set_model("Moskvich 412")
print(bmw.get_model())
bmw.set_year("1985")
print(bmw.get_year())
bmw.set_maker("АЗЛК")
print(bmw.get_maker())
bmw.set_power("25 л. с.")
print(bmw.get_power())
bmw.set_color("баклажан")
print(bmw.get_color())
bmw.set_price("15 000")
print(bmw.get_price())



