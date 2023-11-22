num1={1,2,3,4}  #list1
num2={8,7,6,5,7,8,9}  #list2

print(num1)
print(num2)

#set functions
print(len(num1))

print(max(num1))

print(min(num2))

print(sum(num2))

print(enumerate(num1))

print(any(num2))

print(all(num1))

#set methods
num1.add(5)
print(num1)

num1.update([6,7])
print(num1)

num1.remove(7)
print(num1)

print(num1)
print(num2)
num3=num1.intersection(num2)
print(num3)

num4=num1.difference(num2)
print(num4)

print(num2.pop())

#frozenset
set1=frozenset({1,2,3,4,5,6})
set2=frozenset({9,8,7,6,5})
print(set1)
print(set2)
set3=set1.union(set2)
print(set3)

set4=set1.intersection(set2)
print(set4)

set5=set1.difference(set2)
print(set5)

set6=set1.isdisjoint(set2)
print(set6)
