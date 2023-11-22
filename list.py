numbers=[1,2,3]  #list1
print(numbers)

numbers[2]=4  #change element of index 2
print(numbers)

print(numbers[0])#print index 0

print(numbers)   #print list

print(len(numbers))  #print length of list

print(max(numbers))   #print maximum value

print(min(numbers))   #print minimum value

b=[5,7,8]    #list2

numbers.extend(b)  #add two list
print(numbers)

numbers.append(12)  #add a new element
print(numbers)

numbers.sort(reverse=True) #print reverse of list
print(numbers)

print(numbers.index(2)) #print index number of two

numbers.remove(12) #remove 12
print(numbers)

print(numbers.pop(1)) #popped element of index 1

print(numbers.pop(-1)) #popped element in reverse
      
numbers.insert(4,14)
print(numbers)

'''k=["a","b","c"]
numbers.copy(k)
print(numbers)
