import csv

with open("data2.csv") as f:
    file_reader = csv.reader(f, delimiter=";")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"The file contains columns: {', '.join(row)}")
        else:
            print(f"\t\t\t\t\t\t\t{row[0]}\t\t {row[1]}\t {row[2]}\t{row[3]}")
        count += 1
