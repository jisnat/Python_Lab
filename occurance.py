s=input("Enter a sentence:")
word=s.split()
print(word)
for i in word:
    print(f"{i} occur {word.count(i)} times")
