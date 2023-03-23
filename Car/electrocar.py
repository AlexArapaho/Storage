from Car import classcar

class ElectroCar(classcar.Car):
    def __init__(self, brand, model, year, miles):
        super().__init__(brand, model,year, miles)
        self.battery = 100

    def description_battery(self):
        print(f"Автомобиль имеет мощность {self.battery}%")







