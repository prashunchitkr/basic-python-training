# normal function definition anc call
def function(x, y, z):
    return x, y, z

print(function(1, 2, 3))

# function expression with lambda
fun = lambda x, y, z : (x, z, y)
print(fun(1, 2, 3))

# squaring list in elements using map and lambda
l = list(range(10))
print(list(map(lambda x : x*x, l)))

# normal fizzbuzz function
def fizzbuzz(x):
    if (x%3 == 0 and x%5== 0):
        print('fizzbuzz')
    elif(x%3 == 0):
        print('fizz')
    elif(x%5 == 0):
        print('buzz')

# using lambda
fizzbuzz =  lambda x : 'fizzbuzz' \
            if (x%3==0 and x%5==0) \
            else ('fizz' if x%3==0 \
            else ('buzz' if x%5==0 \
            else x))

print(list(map(fizzbuzz, list(range(1, 16)))))

# IIFE
print((lambda x : x*x)(5))