list1=[]
with open('demo.txt','r')as file:
    for line in file:
        list1.append(line.split())
print(list1)
