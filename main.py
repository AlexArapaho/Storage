# print("Выполнил задание \n\t\t\tГрибов Александр Валерьевич, \n\t\t\t\t\t\t\t\t\tслушатель группы Python214")
#
# print()
import json
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

# import json
# from random import choice
#
#
# def get_person():
#     name = ''
#     tel = ''
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         "name": name,
#         "tel": tel
#     }
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('person.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('person.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person())

# import time
# def deco(func):
#     def wrap(y):
#         print(func(y))
#         return func(y)**65
#     return wrap
#
#
# a = time.monotonic()
# @deco
# def num(x):
#     return x**85
#
#
# print(num(3))
# b = time.monotonic()
#
# c = b - a
# print(c)


# def func1(a):
#     def func2(b):
#         return a * b
#
#     return func2
#
#
#
# x = func1(2)
# print(x(3))
#
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(response)
# todos = json.loads(response.text)
# print(type(todos))
# print(todos)

# import csv
#
# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     print(file_reader)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы {', '.join(row)}")
#         else:
#             print(f"\t\t\t\t\t\t\t{row[0]}-{row[1]}. Родился в {row[2]}")
#         count += 1

# import requests
# import json

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(response)
# todos = json.loads(response.text)
#
#
# todos_by_user = {}
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#             print(todos_by_user)
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#             print("*", todos_by_user)


# class Pet:
#     def __init__(self, name):
#         self.name = name
#
#     def show_name(self):
#         print(f"{self.name}")
#
#     def show_species(self):
#         print(f"{type(self).__name__}")
#
# class Dog(Pet):
#     def __init__(self, sound, name):
#         self.sound = sound
#         super().__init__(name)
#
#
#     def chase_cat(self):
#         print("I'm chasing cats")
#
#     def make_sound(self):
#         print(f"{self.sound}")
#
#
# class Cat(Pet):
#     def __init__(self, name,  sound="mew"):
#        super().__init__(name)
#     def catch_mouse(self):
#         print("I'm catching mice")
#
#
#
#
# p = Cat("Барсик")
# p.show_species()
# p1 = Dog("bark", "Барсик")
# p1.show_species()
# p1.make_sound()
# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def print_info(self):
#         print("This is basic class")
#
# class Clerk(Employee):
#     def print_info(self):
#         print(self.name, self.age)
#
# p = Clerk("Ivanov", 32)
# p.print_info()

# n = int(input("Number of IP addresses: "))
# m = [input("Enter IP-address: ") for i in range(n)]
# y = []
# dct = {}
# for i in m:
#     a = (list(map(int, i.split("."))))
#     a.reverse()
#     z = []
#     for j in range(len(a)):
#         b = a[j]**j
#         z.append(b)
#     c = sum(z)
#     dct[i] = c
#     y.append(c)
# for i in sorted(dct.items()):
#     print(i[0])


# a = [1, [2, 3]]
# b = a
# c = a[:]
#
# a[1][0] = 1
# print(b, c)


import csv

# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     print(file_reader)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы {', '.join(row)}")
#         else:
#             print(f"\t\t\t\t\t\t\t{row[0]}-{row[1]}. Родился в {row[2]}")
#         count += 1

# with open("data.csv") as f:
#     fn = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=fn)
#     count = 0
#     for row in file_reader:
#         print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы {', '.join(row)}")
#         print(f'{row["Имя"]} - {row["Профессия"]}. Родился в {row["Год рождения"]} году.')
#         count += 1
#     print(f'Всего в файле {count} строки')

# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

# with open('sw_data1.csv', 'w') as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 12})
#     writer.writerow({"Имя": "Вова", "Возраст": 15})

# data = [{
#
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
#
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_data1.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

from bs4 import BeautifulSoup


# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", class_="row")[1].find(class_="name").text
# row = soup.find_all("div", {"data-set": "salary"})
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None


# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# import re
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.search(pattern, s).group()
#     res = re.findall(pattern, s)[0]
#     print(res)
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", {"data-set": "salary"})
# for i in row:
#      get_salary(i.text)



# res = requests.get("https://ru.wordpress.org/")
# # print(res.headers['content-type'])
# # print(res.content)
# #
#
# print(res.text)
# import requests
#
#
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     print(p1)
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     get_data(get_html(url))
#
# if __name__ == '__main__':
#     main()
#
# import requests
# import re
#
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open('plugings.csv', 'a') as f:
#         write = csv.writer(f, delimiter=";", lineterminator="\r")
#         write.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("article")
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find('span', class_="rating-count").find("a").text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#         print(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
# if __name__ == '__main__':
#     main()


# import requests
#
#
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a', encoding='utf-8-sig') as f:
#         write = csv.writer(f, delimiter=';', lineterminator="\r")
#         write.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ""
#
#         try:
#             url = el.find('h3').find('a').get("href")
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_="entry-excerpt").text.strip()
#         except ValueError:
#             snippet = ""
#
#         try:
#             active = el.find('span', class_="active-installs").text.strip()
#         except ValueError:
#             active = ''
#
#         try:
#             c = el.find('span', class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ''
#
#         data = {
#            'name': name,
#            'url': url,
#            'snippet': snippet,
#            'active': active,
#            'cy': cy
#                }
#         write_csv(data)
#
#
# def main():
#     for i in range(5, 26):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

from parse import Parser


def main():
    pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
    pars.run()



if __name__ == '__main__':
    main()



