a = 10

a > 1 and print('this print statement is executed')
a > 3 and print('this print statement is not executed')
temp = 0
a > 1 and temp != 0 and print(a / temp)

#using or
a == 2 or print('this will not get executed')
a == 1 or print('this will get executed')

'''
if True {
    print('this is in other programming languages like c')
}

'''
if False:
    print('False')
    print('False')
    print('False')

if True:
    print('True')
    print('True')
    print('True')


a = 10
b = 5

#alternate execution
if a > b : #flase
    print('it is true')
else:
    print('not true ')


#chained condition
if a == 3 : #flase
    print('it is true')
elif a == b:
    print('both are equal')
elif a == 4:
    print(' a is 4')
else:
    print('none')


#nested condition
if a == b:
    print('equal')
else:
    if a > b:
        print('a is greater than b')
    else:
        print('b is greater than a')
