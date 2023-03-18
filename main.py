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

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Я кот. Меня зовут {self.name}, мне {self.age} лет')

    def make_sound(self):
        print(f'{self.name} мяукает')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Я собака. Меня зовут {self.name}, мне {self.age} лет')

    def make_sound(self):
        print(f'{self.name} гавкает')

p1 = Cat("Пушок", 2.5)
p2 = Dog("Мухтар", 4)
a = [p1, p2]

for i in a:
    i.info()
    i.make_sound()















