# local
# def paral(a, b, c):
#     def rec(i, j):
#         return i*j
#     s = 2*(rec(a, b) + rec(b, c) + rec(a, c))
#     return s
#
#
# print(paral(2, 4, 6))
# print(paral(5, 8, 2))
# print(paral(1, 6, 8))



# nonlocal
# def paral(a, b, c):
#     s = 0
#
#     def rec(i, j):
#        nonlocal s
#        s += i*j
#     rec(a, b)
#     rec(b, c)
#     rec(a, c)
#     return 2*s
#
#
# print(paral(2, 4, 6))
# print(paral(5, 8, 2))
# print(paral(1, 6, 8))


# global
# def paral(a, b, c):
#     global s
#     def rec(i, j):
#         return i*j
#     s = 2*(rec(a, b) + rec(b, c) + rec(a, c))
#     return s
#
#
# paral(2, 4, 6)
# print(s)
# paral(5, 8, 2)
# print(s)
# paral(1, 6, 8)
# print(s)


