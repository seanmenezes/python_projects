import csv

with open("data.csv") as file:
    reader = csv.reader(file)
   # print(list(reader))
    print("\n print csv:")
    for row in reader:
        print(row)