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

import os

def rem_dir(x):
    print("Deleting folders: ")
    print("=" * 30)
    # print(os.listdir(x))
    for root, dirs, files in os.walk(x):
        if not os.listdir(root):
            os.rmdir(root)
            print(f"folder {root} deleted")
    print("=" * 30)

rem_dir("test")

# for root, dirs, files in os.walk("test"):
#     print("root:", root)
#     print("dirs:", dirs)
#     print("files:", files)












