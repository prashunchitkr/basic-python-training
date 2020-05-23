#generators
#yield 
#generator func always returns an iterator

#def square(num):
#    #return num **2
#    yield(num**2)

#print(dir(square(10)))
#test = square(10)
#print(next(test))


def my_gen(a):
    return a
    a += 1

print(my_gen(0))
print(my_gen(0))

def my_gen():
    a = 0
    print('First')
    yield a

    a += 1
    print('Second')
    yield a

    a += 1
    print('final')
    yield a

temp = my_gen()
print(next(temp))
print(next(temp))
print(next(temp))
#print(next(temp))

#my gen function returns iterator()
for i in my_gen():
    print(i)

#class Object:
#    def next()
#
#    def iter()

def test():
    a = 0
    while True:
        yield a
        a += 1
        #print(a)

temp = test()
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))

for i in test():
    print('hello')
