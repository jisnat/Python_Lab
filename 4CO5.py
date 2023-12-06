import csv
with open('exelemploye.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("Name")
    print("---")
    for i in data:
        print(i['NAME'])
