lst1 = [5, 9, 6, 7]
lst2 = [3, 11, 8]
lst3 = [2, 4]
lst4 = [10, 1, 12]
lst = lst1 + lst2 + lst3 + lst4
print(lst)

type_of_sort = int(input("Ввведите желаемый вид сортировки, 1 - по уб., 2 - по возр.: "))
numb = int(input("Введите значение для поиска: "))

def sort_and_search(x, y, z):
    for i in range(len(x) - 1):
         for j in range(len(x) - i - 1):
            if y == 1:
                if x[j] < x[j + 1]:
                    x[j], x[j + 1] = x[j + 1], x[j]
            elif y == 2:
                if x[j] > x[j + 1]:
                    x[j], x[j + 1] = x[j + 1], x[j]
            else:
                print("Вид сортировки указан неверно")
    found = False
    pos = 0
    while not found and pos < len(x):
        if x[pos] == z:
            found = True
            print(f'Число {z} найдено')
        else:
            pos +=1
    if found == False:
        print(f'Число {z} не найдено')
    print(lst)

sort_and_search(lst, type_of_sort, numb)
