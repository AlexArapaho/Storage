num = int(input("Введите число от 0 до 99: "))
if 0 <= num <= 99:
    print(num, end=" ")
    if (num - int(num/10)*10) == 1 and num != 11:
        print("копейка")
    elif (2 <= (num - int(num/10)*10) <= 4) and (num != 12) and (num != 13) and (num != 14):
        print("копейки")
    else:
        print("копеек")
else:
    print("Ошибка ввода")