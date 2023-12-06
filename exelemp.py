import csv
with open('exelemploye.csv','r')as file1:
    reader=csv.reader(file1)
    for row in reader:
        print(row)
