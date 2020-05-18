'''
Dictionary Operations
1. Adding items
2. retriving items
3. get()
4. update()
5. items()
6. keys()
7. values()
'''

person = {
    'name': 'John Doe',
    'age': 20,
    'gender': 'm'
}

print(person)

# inserting
person['country'] = 'Nepal'
person['hobbies'] = ['sports', 'reading']
person['pet_names'] = {
    'cat': 'oatmeal'
}
print(person)

# # retreval
print(person['name'])
print(person.get('surname', 'not found'))
print(person.get('country', 'not found'))

# deleting key value pair
del person['age']
print(person)

# .items() .keys() .values()
print(person.items())
print(person.keys())
print(person.values())

# updating a existing key value pair
person['country'] = 'US'
print(person)


# iterating
for i in person.values():
    print(i)

for i in person.keys():
    print(f'{i}->{person[i]}')

for key, val in person.items():
    print(f"person[{key}]: {val}")
