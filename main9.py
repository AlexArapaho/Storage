# Задание 1
# d = {"emp1": {"name": "John", "salary": 7500}, "emp2": {"name": "Emma", "salary": 8000},
#      "emp3": {"name": "Brad", "salary": 6500}}
# print(d["emp3"])
#
# d["emp3"]["salary"] = 8500
# print(d["emp3"])


# Задание 2
# def students():
#     sm = 0
#     d = dict()
#     n = int(input("Количество студентов: "))
#     for i in range(n):
#         name = input("Студент: ")
#         points = int(input("Балл: "))
#         d[name] = points
#         sm += points
#     print(d)
#     med = sm/n
#     print("Количество студентов: ", n)
#     print("Средний балл: ", med,".", "Студенты с баллом выше среднего: ")
#     for j in d:
#         if d[j] > med:
#             print(j)
# students()

# d = {"a": 1, "b": 2, "c": 3}
# value = d.get("f", "Такого ключа нет")
# print(value)
#
# n = d.keys()
# n = d.values()
# n = d.items()
#
# for i, j in d.items():
#     print(i, "->", j)

# методы keys, values, items, copy, pop,
# popitem (удаляет произвольную пару), setdefault (добавляет ключ со значением, если ег не существует)
# update (обавляет ключ и значение, если ключ был - перезапишет его значение на новое)

# x = {"a": 1, "b": 2}
# y = {"c": 3, "d": 4}
#
# z = x.copy()
# z.update(y)
#
# print(z)
#
# z = x | y
# print(z)

sales = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4738, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3908, "S": 3645, "E": 8821, "W": 2451}
}

for x in sales:
    print(x)
    for y in sales[x]:
        print('\t', y, ": ", sales[x][y], sep="")


