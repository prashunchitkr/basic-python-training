'''
List Operations
1. append(x)
2. extend(iterable)
3. insert(i, x)
4. remove(x)
5. pop([i])
6. clear()
7. sort()
8. copy()
9. count()
'''


days = ['Sunday', 'monday', 'tuesday']


# append()
days.append('wednesday')
print(days)

days.append('thursday')
print(days)


# extend()
days.extend(['friday', 'saturday'])
print(days)


# insert()
days.insert(3, 'random day')
print(days)

days = days[:3] + ['random day 2', 'random day 3'] + days[3:]
print(days)


# remove()
days.remove('random day 3')
days.remove('random day 2')
days.remove('random day')
print(days)

# removing multiple items
days = days[:2] + days[4:]
print(days)


# pop()
days.pop(1)
print(days.pop(1))
print(days)


# sort()
some_arr = [10, 42, 235, 1, 13, 134]
some_arr.sort()
print(some_arr)


# reversal
print(days[::-1])
days.reverse()
print(days)


# list and tuple unpacking
sun, mon, tue = days
print(sun, mon, tue)

days = tuple(days)
sun, mon, tue = days
print(sun, mon, tue)

a_list = [1, 2, 3]
one = a_list[0]
two = a_list[1]
three = a_list[2]
print(one, two, three)

one, two, three = a_list
print(one, two, three)


# checking if an item is in list
for day in days:
    if day == 'Sunday':
        print(True)

print('Sunday' in days)
