# range(start, end, step) #it is a built in function to generate list 

a = [1, 2, 3, 4, 5]
a = ['lucky', 'prashun', 'me', 'students']
for i in a:
    print(i, end='\t')
    print(a)


for i in range(5):
    for j in range(5):
        print(i, j)

persons = ['lucky', 'prashun', 'me', 'students']
for index, value in enumerate(persons):
    print(index, value)

for i in enumerate(persons):
    print(i)

#if we use enumerate
# a, b = [1, 2]
#0, lucky
# 1, prashun

a = [12, 3, 123, 213, 213, 12]
#totoal sum of list values
sum = 0
for i in a:
    sum = sum + i
print('the value of sum is: ', sum)

#largest among the list
largest = None
for i in a:
    if largest is None or i > largest:
        largest = i

print('largest value is: ', largest)

#built in python functions
print(max(a))
print(min(a))

#fizz buzz game
'''
1 - 1000
divisible by  3 fizz
divisible by 5 buzz
both fizz buzz
1
2
3 fizz
4
5 buzz
6
7
8
9 fizz
10
11
12
13
14
15 fizz buzz
'''

#fizz buzz unoptimized method
for i in range(1, 50):
    if i % 5 == 0 and i% 3 == 0:
        print('fizz buzz')
    elif i % 3 == 0 :
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)


#fizz buzz optimized method
for i in range(1, 50):
    output = ''
    if i % 3 == 0 :
        output = output + 'fizz'
    
    if i % 5 == 0:
        output = output + 'buzz'

    if output == '':
        output = i
    print(output)


#dictionary in for loop
person = {'name':'test', 'age': 10, 'address': 'kathmandu' }
for i in person:
    print(i, end=': ')
    print(person[i])
