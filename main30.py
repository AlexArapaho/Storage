import json


class Countries:
    def __init__(self, filename, country=None):
        self.country = {}
        self.filename = filename

    def reading(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            self.country = json.load(f)

    def record(self):
        with open(self.filename, 'w', encoding="utf-8") as f:
            json.dump(self.country, f)

    def add_country(self, x=None, y=None):
        x = input("Введите название страны с заглавной буквы: ")
        y = input("Введите название столицы с заглавной буквы: ")
        try:
            self.reading()
            self.country[x] = y
            self.record()
        except FileNotFoundError:
            self.country[x] = y
            self.record()
        print("*" * 30)
        print("Файл сохранён")
        return self.country

    def del_country(self, x=None):
        try:
            x = input("Введите название страны с заглавной буквы: ")
            del(self.country[x])
            self.record()
            print("*" * 30)
            print("Элемент удалён")
            # return self.country
        except KeyError:
            print("*" * 30)
            print("Такой страны нет в списке")

    def find_country(self, x=None):
        try:
            x = input("Введите название искомой страны: ")
            print("*" * 30)
            print(f"Элемент, который вы искали: {x}:{self.country[x]}")
        except KeyError:
            print("*" * 30)
            print("Такой страны нет в списке")

    def display_data(self):
        try:
            self.reading()
            print("*"*30)
            print(f"Список стран и столиц: {self.country}")
        except FileNotFoundError:
            print("*" * 30)
            print("Список ещё не создан")

    def edit_data(self, a=None, b=None):
        a = input("Введите название страны, данные о которой нужно изменить: ")
        print(self.country)
        if a in self.country:
            b = input("Введите новое название столицы: ")
            self.reading()
            self.country[a] = b
            self.record()
            print("*" * 30)
            print("Данные изменены")
            # return self.country
        else:
            print("*" * 30)
            print("Такой страны ещё нет в списке")


    def interact(self, a=True):
        while a:
            sel = input("Выбор действия:\n"
                  "1 - добавление данных\n"
                  "2 - удаление данных\n"
                  "3 - поиск элемента\n"
                  "4 - редактирование данных\n"
                  "5 - просмотр данных\n"      
                  "6 - завершение работы\n"
                  "Ввод: ")
            if sel == "1":
                self.add_country()
            elif sel == "2":
                self.del_country()
            elif sel == "3":
                self.find_country()
            elif sel == "4":
                self.edit_data()
            elif sel == "5":
                self.display_data()
            elif sel == "6":
                a = False
                print("*" * 30)
                print("Работа завершена")
                return
            else:
                print("*" * 30)
                print("Выберите из предложенных вариантов")


p = Countries("countries.json")
p.interact()











