#
file_name = "text.txt"
txt = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n"
with open(file_name, "w+") as f:
    f.write(txt)

with open(file_name, "r+") as f:
    rf = f.readlines()

# Задание 1 Транспозиция 2-х строк
# rf[1], rf[2] = rf[2], rf[1]
#
# with open(file_name, "w+") as f:
#     f.writelines(rf)

# Задание 2 Реверсирование
# rf.reverse()
# with open(file_name, "w+") as f:
#     f.writelines(rf)

# Задание 3 Объединение файлов
# file_name1 = "text1.txt"
# file_name2 = "text2.txt"
# txt1 = "Первый файл."
# txt2 = "Второй файл."
# with open(file_name1, "w") as f1, open(file_name2, "w") as f2:
#     f1.write(txt1)
#     f2.write(txt2)
# with open(file_name1, "r") as f1, open(file_name2, "r") as f2:
#     txt3 = f1.readlines() + f2.readlines()
# file_name3 = "text3.txt"
# with open(file_name3, "w") as f3:
#     f3.writelines(txt3)









