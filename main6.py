# Задание 1

# from math import sqrt, pi
#
# while True:
#
#     n = int(input("Выберите фигуру. 1 - треугольник, 2 - прямоугольник, 3 - круг: "))
#     if n == 1:
#         a = int(input("Введите сторону a: "))
#         b = int(input("Введите сторону b: "))
#         c = int(input("Введите сторону c: "))
#         p = (a + b + c)/2
#         s = sqrt(p*(p - a)*(p - b)*(p - c))
#         print("Площадь круга равна", s)
#         break
#     elif n == 2:
#         a = int(input("Введите сторону a: "))
#         b = int(input("Введите сторону b: "))
#         s = a*b
#         print("Площадь прямоугольника равна", s)
#         break
#
#     elif n == 3:
#         r = int(input("Введите радиус: "))
#         s = pi*(r**2)
#         print("Площадь прямоугольника равна", s)
#         break

# Задание 2
# w = 4
# h = 3
# matrix = [[x + row*4 + 1 for x in range(w)] for row in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
# print("\n")
#
# for x in range(w):
#     for row in range(h):
#         print(matrix[row][x], end="\t")
#     print()

# Задание 3
# import random
#
# w = 6
# h = 6
# matrix = [[random.randint(0, 10) for x in range(w)] for y in range(h)]
# for y in matrix:
#     for x in y:
#         print(x, end="\t")
#     print()
# print("\n")
#
# line = [random.randint(0, 10) for a in range(6)] # одномерный список
# print(line)
# print("\n")

# for y in matrix:
#     if matrix.index(y) % 2 == 0:
#        y = line
#     for x in y:
#         print(x, end="\t")
#     print()


# Задание 4
# import random
#
# w = 6
# h = 6
# matrix = [[random.randint(0, 10) for x in range(w)] for y in range(h)]
# for y in matrix:
#     for x in y:
#         print(x, end="\t")
#     print()
# print("\n")
# matrix[0], matrix[1] = matrix[1], matrix[0]
# matrix[2], matrix[3] = matrix[3], matrix[2]
# matrix[4], matrix[5] = matrix[5], matrix[4]
# for y in matrix:
#     for x in y:
#         print(x, end="\t")
#     print()





















