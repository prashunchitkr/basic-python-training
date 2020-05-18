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


# set opertations

summer = {'banana', 'watermelon', 'grapes', 'lemon', 'berries'}
winter = {'orange', 'banana', 'pineapple', 'lemon', 'kiwi'}
spring = {'watermelon', 'grapes'}

print('summer: ', summer)
print('winter: ', winter)

print('union: ', summer | winter)
print('intersection: ', summer & winter)
print('difference: ', summer - winter)
print('symmetric difference: ', summer ^ winter)

print('subset: ', spring <= summer)
# returns True if spring is subset of summer else False

print('superset: ', summer >= spring )
# returns True if summer is superset of spring else False