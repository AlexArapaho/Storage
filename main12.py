
# Задание 1
# from math import pi
#
# print((lambda r: pi*r**2)(2))
# print((lambda x, y: x*y)(10, 13))
# print((lambda a, b, h: ((a+b)/2)*h)(7, 5, 3))


# Задание 2
# print((lambda x, y, z: x*y*z)(2, 5, 5))


# Задание 3 и 4
# lst = [{"name": "Jannifer", "final": 95},
#        {"name": "David", "final": 92},
#        {"name": "Nikolas", "final": 98}]
# res = sorted(lst, key=lambda item: item["final"], reverse=True)
# print(res)
#
# lst2 = [lst[i]["final"] for i in range(len(lst))]
#
# for i in lst:
#        if i["final"] == min(lst2):
#               print("Студент с минимальной оценкой - ", i)
#        elif i["final"] == max(lst2):
#               print("Студент с максимальной оценкой - ", i)



# Задание 5
# lst = [3, 6, 8, 9, 1, 2]
# lst2 = list(map((lambda x: x*lst.index(x)**3), lst))
# print(lst2)

# Задание 6
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# print(list(map(lambda x: x**2, nums)))
# print(list(map(lambda x: x**3, nums)))
