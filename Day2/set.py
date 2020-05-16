# set

fruits = {'orange', 'watermelon'}
print(fruits, type(fruits))

# empty set
fruits = set()
print(fruits, type(fruits))

fruits = {'orange', 'watermelon', 'grapes', 'mango', 'apple'}
print(fruits)

fruits = {'orange', 'watermelon', 'grapes', 'mango', 'apple', 'orange'}
print(fruits)

# not accessible
# fruits[0]

# mutable
fruits.add('papaya')
print(fruits)

# immutable
vegetable = frozenset({'carrot', 'tomato', 'potato'})
print(vegetable)
