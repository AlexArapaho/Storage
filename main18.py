# lst = [-2, 3, 8, -11, -4, 6]
# count = 0
# def count_neg(x):
#     global count
#     if len(x) == 0:
#         print("Количество отрицательных элементов: ", count)
#     elif x[0] < 0:
#         count += 1
#         x = x[1:]
#         count_neg(x)
#     elif x[0] > 0:
#         x = x[1:]
#         count_neg(x)
#
# count_neg(lst)


# Дополнительное задание
# name = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# def foo(x):
#     name2 = []
#     global count
#     count = 0
#     while len(x) != 0:
#         if isinstance(x[0], list):
#             name2 = name2 + [i for i in x[0]]
#             x = x[1:]
#             if len(x) == 0 and name2 != 0:
#                 x = name2
#                 name2 = []
#             elif len(x) == 0 and name2 == 0:
#                 break
#         else:
#             count += 1
#             x = x[1:]
#             if len(x) == 0 and name2 != 0:
#                 x = name2
#                 name2 = []
#             elif len(x) == 0 and name2 == 0:
#                 break
#
#     print("Всего элементов: ", count)
#
#
# foo(name)








