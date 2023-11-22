details={
    'name':'jisna',
    'age':21,
    'gender':'female',
    }

print(details)

#dictionary functions
print(len(details))
print(type(details))
print(str(details))

#dictionary methods
print(details.get('name'))
print(details.keys())

print(details.items())

details.update({'place':'mukkam'})
print(details)

print(details.values())
print(details)

print(details.pop('place'))
