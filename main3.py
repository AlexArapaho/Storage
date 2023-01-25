# Задание 1.
a = int(input("Введите количество символов: "))
b = int(input("Задайте ориентацию линии, 0 - горизонтальная, 1 - вертикальная: "))
i = 0
while i < a:
    if b == 0:
        print("@", end="")
    elif b == 1:
        print("@")
    else:
        b = int(input("Задайте ориентацию линии, 0 - горизонтальная, 1 - вертикальная: "))
    i += 1


# Задание 2
# length = 17
# width = 5
# i = 0
# while i < width:
#     j = 0
#     if i%2 == 0:
#         while j < length:
#             print("+", end="")
#             j += 1
#         else:
#             print()
#     elif i % 2 == 1:
#         while j < length:
#             print("-", end="")
#             j += 1
#         else:
#             print()
#     i += 1


# Задание 3
# a, b, c = 1, 2, 3
# maxim = a if (a > b and a > c) else b if (b > a and b > c) else c
# print(maxim)

# Задание 4
# op = int(input("Выберите операцию(1-r, 2-+, 3--, 4-/, 5-*, 6-%, 7-<, 8->): "))
# if op == 1:
#     a = int(input("Введите число: "))
#     print(-a)
# else:
#     x = int(input("Введите первое число: "))
#     y = int(input("Введите второе число: "))
#     if op == 2:
#         print(x+y)
#     elif op == 3:
#         print(x-y)
#     elif op == 4:
#         try:
#             print(x/y)
#         except ZeroDivisionError:
#             print("На ноль делить нельзя!")
#     elif op == 5:
#         print(x*y)
#     elif op == 6:
#         print(x%y)
#     elif op == 7:
#         print(x if x < y else y)
#     elif op == 8:
#         print(x if x > y else y)
#     else:
#         print("Некорректный код операции")



