class Car:
    def __init__(self, brand, model, year, miles):
        self.brand = brand
        self.model = model
        self.year = year
        self.miles = miles

    def show_car(self):
        print(f"{self.brand}, {self.model}, {self.year} год, {self.miles} км")