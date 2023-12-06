with open('file3.txt','w')as file:
    file.write('hai jisna')


list1=[]
with open('file3.txt','r')as file:
    for line in file:
        list1.append(line.split())
print(list1)
