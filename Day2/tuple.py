# tuple

# empty tuple
fruits = ()
print(fruits, type(fruits))

# empty tuple
fruits = tuple()
print(fruits, type(fruits))

# define tuple of fruits
fruits = ('orange', 'watermelon', 'grapes', 'mango', 'apple')
print(fruits, type(fruits))

orange = fruits[0]
watermelon = fruits[1]
grapes = fruits[2]

print(orange, watermelon, grapes)

# slicing
# get tuple of fruits from index 0 to 2
summer_fruits = fruits[0:3]
print(summer_fruits)

# get tuple of fruits from 3 to end
winter_fruits = fruits[3:]
print(winter_fruits)

# get second-last fruit
print(fruits[-2])

# get tuple of fruits from index 1 to 2
print(fruits[1:3])

# tuple[start:end:step]
print(fruits[0:4:2])


# immutable
# cannot replacing orange with banana
# fruits[0] = 'Banana'
# print(fruits)

# total fruits in a tuple
print(len(fruits))