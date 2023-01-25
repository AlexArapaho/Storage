# lst1 = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
# lst2 = []
# s = 0
#
# for i in lst1:
#     if i == 1:
#         s = lst1.pop(lst1.index(i))
#         lst2.append(s)
#     for j in range(2, i + 1):
#         if i % j != 0 and i != j:
#             continue
#         elif i % j == 0 and i == j:
#             continue
#         elif i % j == 0 and i != j:
#             s = lst1.pop(lst1.index(i))
#             lst2.append(s)
#             break
# print("Простые числа", lst1)
# print("Остальные числа", lst2)
#
# print("Минимальное простое число:", min(lst1))
# print("Максимальное число, не являющееся простым:", max(lst2))




