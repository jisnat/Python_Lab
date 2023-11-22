list1=[2,5,-9,8,7,3,14,-1]
list2=[]
for i in list1:
    if i<0:
       list2.append(i)
print(list2)

list3=[i for i in list1 if i>0];
print(f"positive list is {list3}")

list4=[i**2 for i in list1]
print(f"sguare list is {list4}")

word=input("Enter a word:")
vowel=[i for i in word if i in 'aeiouAEIOU']
print(f"The vowels are {vowel}")
ordinals=[ord(i)for i in word]
print(ordinals)
