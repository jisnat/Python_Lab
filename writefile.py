'''file=open('file1.txt','w')
file.write('hello world !')

file=open('file1.txt','r')
re=file.read()
print(re)
file.close()'''



#do not need close funtion 
with open('file3.txt','w')as file:
    file.write('hai jisna')
    
