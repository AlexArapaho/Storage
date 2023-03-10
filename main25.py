class Student:
    def __init__(self, name):
        self.name = name
        self.lt = self.Laptop()

    def print_inf(self):
        print(self.name, "=>", self.lt.model, self.lt.cpu, self.lt.memory)

    class Laptop:
        def __init__(self):
            self.model = "HP"
            self.cpu = "i7"
            self.memory = "16"


std = Student("Roman")
std.print_inf()
std = Student("Vladimir")
std.print_inf()

