a = 5
# a = a //5 
a /=2
print(a)
# a += 1
# a *= 1
# a /= 1
# a //= 1

#is
a = 3
b = 3
print('id of a is: ', id(a))
print('id of b is: ', id(b))

a = [1, 2, 3]
b = [1, 2, 3]
print('id of a is: ', id(a))
print('id of b is: ', id(b))
print( a is b)
print( a is not b)
print(not False) #!=

persons = ['john', 'jordan', 'musk', 'lambda']

for i in enumerate(persons, 100):
    print(i)

'''type conversion implict, explict'''
a = 5
b = 2.12
c  = a + b
print('type of a: ', type(a))
print('type of b: ', type(b))
print('type of c: ', type(c))

# float()
# str()
# list()
# dict()


a = '123'
b = 1
print('type of a: ',type(int(a)))
print('sum =: ', int(a) + b)

print(int('0b1010', 2))
print(int('0o12', 8))

print(type(str(123)))
float(123)
int(123.1232)
int('asdfasdfsdaf')
print(set([1, 2, 3, 3, 2]))
print(dict( [('abc', 1), ('asdf', 2)] ))
print(list('asdfasdfsfd'))
print(tuple([1, 2, 3, 4]))

a = 3
if(a < 5):
    pass #noop

for i in range(10):
    break

for i in range(10):
    print(i)
else:
    print('fully executed')

for i in range(10):
    print(i)
    if i == 4:
        break
else:
    print('fully executed')

for i in range(10):
    print(i)
    if i == 4:
        continue
else:
    print('fully executed')

a = 10
while a > 0:
    print(a)
    a -= 1
else:
    print('fully executed')

#negative indexing
print(list(range(10, 5, -1)))
print(list(range(-10, -5, 1)))