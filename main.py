# print("Выполнил задание \n\t\t\tГрибов Александр Валерьевич, \n\t\t\t\t\t\t\t\t\tслушатель группы Python214")
#
# print()

#
#
# def deco(func):
#     def wrap(y):
#         print(func(y))
#         return func(y)*3
#     return wrap
#
#
# @deco
# def num(x):
#     return x
#
# print(num(9))
#


# print("Hello")

#
# str1 = "Замените в этой строке все появления буквы 'о' кроме первого и последнего вхождения"
# str2 = str1.replace("о", "О")
# print(str2)

# def foo(x):
#     if sum(x[0:3]) == sum([x[3:7]]):
#         print("Это счастливое число!")
#     else:
#         print("Это несчастливое число")
#
# foo("123321")

# x = input()
# a = x[0:3]
# b = x[3:7]
# t1 = t2 = 0
# for i in a:
#     t1 = t1 + int(i)
# for j in b:
#     t2 = t2 + int(j)
# if t1 == t2:
#     print("счастливое число")
# else:
#     print("nope")
# print(t1)
# print(t2)

# import random
#
# a = [random.randint(0, 100) for i in range(10)]
# print(a)
# b = int(input("Enter a number: "))
#
# def search_of(x):
#     found = False
#     for i in range(len(x)):
#         if x[i] == b:
#             print(f'The number {b} is found')
#             found = True
#             break
#
#     if found == False:
#         print(f'The number {b} is not found')

# import os
#
# def rem_dir(x):
#     print("Deleting folders: ")
#     print("=" * 30)
#     # print(os.listdir(x))
#     for root, dirs, files in os.walk(x):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"folder {root} deleted")
#     print("=" * 30)

# rem_dir("test")

# for root, dirs, files in os.walk("test"):
#     print("root:", root)
#     print("dirs:", dirs)
#     print("files:", files)
#
# a = {3, 4}
# b = {1, 2}
# c = set()
# i = 0
# j = 0
# for i in a:
#     for j in b:
#         c.add((i, j))
#         i += 1
#         j += 1
#
# print(c)

import re


#
# class UserData:
#     def __init__(self, fio, age, ps, weight):
#         self.verify_fio(fio)
#         self.__age = age
#         self.__password = ps
#         self.__weight = weight
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall("[А-яё-]", fio))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис!")
#     @staticmethod
#     def verify_age(age):
#         if not isinstance(age, int) and age < 18 and age > 120:
#             raise TypeError()
#
# p1 = UserData("Иван Иванович Иванов", 26, "123 321", 80.8)
# p1.verify_fio("Иван Иванович Иванов")

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я кот. Меня зовут {self.name}, мне {self.age} лет')
#
#     def make_sound(self):
#         print(f'{self.name} мяукает')
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}, мне {self.age} лет')
#
#     def make_sound(self):
#         print(f'{self.name} гавкает')
#
# p1 = Cat("Пушок", 2.5)
# p2 = Dog("Мухтар", 4)
# a = [p1, p2]
#
# for i in a:
#     i.info()
#     i.make_sound()

# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             return func(a, b) ** self.arg
#
#         return wrap
#
# @Power(2)
# def um(a, b):
#     return a*b
#
# print(um(2, 3))

# def lst(x):
#     ls = []
#     for i in range(x + 1):
#         ls.append(i)
#     return ls


# def lst(x):
#     return [i for i in range(x + 1)]
#
# print(lst(5))

# from Geometry import rect
#
# r = rect.Rectangle(1, 2)

# import start
#
# start.run()

# from Car import electrocar
#
# def run():
#     car1 = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
#     car1.show_car()
#     car1.description_battery()
#
# if __name__ == '__main__':
#     run()

# import pickle
#
#
# file_name = "basket.txt"
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": 'морковь',
#     "бюдже": 1000}
#
# with open(file_name, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, "rb") as fh:
#     shop_list2 = pickle.load(fh)
# print(shop_list2)

import pickle

# class Test:
#      num = 35
#      st = "Привет"
#      lst = [1, 2, 3]
#      d = {"first": "a", "second": 2}
#      tpl = (22, 36)
#
#      def __str__(self):
#          return f"Число {Test.num}\n строка {Test.st}\n список {Test.lst} \n" \
#                 f"словарь {Test.d}\n кортеж {Test.tpl}"
#
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# new_obj = pickle.loads(my_obj)
# print(new_obj)


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "ghghg"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr["c"]
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x*x


#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)

# data = {
#     'name': 'Olga',
#     'age': 35,
#     True: 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'FirstName': 'Alice',
#             'Age': 6
#         }
#     ]
# }
#
# with open('date.json', 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open('date.json', 'r') as fw:
#     data1 = json.load(fw)
#
# print(data1)
#
# st = json.dumps(data)
# print(st)
#
# data2 = json.loads(st)
# print(data2)

# x = {
#     "name": "Виктор"
# }
# y = {
#     "name": "Виктор"
# }
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))

import json
from random import choice


def get_person():
    name = ''
    tel = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    person = {
        "name": name,
        "tel": tel
    }

    return person


def write_json(person_dict):
    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = []

    data.append(person_dict)
    with open('person.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(get_person())





