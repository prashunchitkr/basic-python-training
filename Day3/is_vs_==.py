#points to same object memory
a = b = 10
temp = 20
temp2 = 20
print('id of a: ', id(a))
print('id of b: ', id(b))
print(a is b)
print('id of temp: ',id(temp))
print('id of temp2: ',id(temp2))
#both are true because both is pointing at same object in memory
#because they have same values
print(temp == temp2)
print(temp is temp2)


#differnce between is and ==
a = [1, 2, 3]
b = [1, 2, 3]

print('address pointed by a: ',id(a))
print('address pointed by b: ',id(b))
print(a == b)
print( a is b)