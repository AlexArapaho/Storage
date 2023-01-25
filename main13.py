# def aver(func):
#     def wrap(*args):
#         print(func(*args))
#         return func(*args)/len(args)
#
#     return wrap
#
#
# @aver
# def summa(*args):
#     return sum(args)
#
#
# print(summa(2, 3, 3, 4))

# def vyz(func):
#     i = 0
#
#
#     def wrap():
#         func()
#         nonlocal i
#         i += 1
#         print("Новый вызов", i)
#
#     return wrap
#
# @vyz
# def hello():
#     print("Hello")
#
# hello()
# hello()
# hello()


# def f1(func):
#     def f2(x):
#         print("code before")
#         print(func(x))
#         print("code after")
#     return f2
#
# @f1
# def f3(x):
#     return 3*x
#
#
# f3(7)

import random
#
# x = {2*i: 4*i for i in range(10)}
# for i,j in x.items():
#     print(i, j)
#
# print(x.items())
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)
#
# b = list(filter(lambda x: x < 5, a))
# print(b)

# print([x for x in a if x < 5])

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = [i for i in b if i in a]
# print(c)


# a = {"a": 56, "b": 89, "c": 15, "d": 42}
#
# print(sorted(a.items(), key=lambda x: x[1]))

# def a(fu):
#     def wr(x, y):
#         print("data: ", x, y)
#         # fu(x, y)
#     return wr
#
# @a
# def b(x, y):
#     print("surname, name: ", x, y)
#
# b("Snow", "John")


def dec(arg1, arg2):
    def dec1(func):
        def wrap(x, y):
            print(arg1, x, arg2, y, "=", end=" ")
            func(x, y)


        return wrap
    return dec1

@dec("Summa", "+")
def sl(x, y):
    print(x + y)

@dec("Raznost", "-")
def vy(a, b):
    print(a - b)


sl(2, 3)

try:
    vy('hui', 4)
except TypeError:
    print("Функция не работает с эттим типом данных")








