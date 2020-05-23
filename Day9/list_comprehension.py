person_name = 'jabriel'
letters = []

for i in person_name:
    letters.append(i)

print(letters)

#[exp for i in....]
letters = [i for i in person_name]
print(letters)

#using lambda
letters = list(map(lambda x: x, person_name))
print(letters)


#even using for loop
even = []
for i in range(10):
    if i%2 == 0:
        even.append(i)

print(even)
#using list comprehension
even = [i for i in range(10) if i%2 == 0]
print(even)

#even for number greater than 5
#list comprehension with multiple if
even = [i for i in range(10) if i%2 == 0 if i > 5]
print(even)
#0, 1, 2

#list comprehension with if else
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#check =  []
#for i in numbers:
#    if i%2 == 0:
#        check.append('even')
#    else:
#        check.append('odd')
#
#print(check)

check = ['even' if i%2 == 0 else 'odd' for i in numbers]
print(check)

#[[1, 2], [1, 2], [1, 2]]
test = []

for i in range(5):
    temp = []
    for j in range(2):
        temp.append(j)
    test.append(temp)

print(test)

temp = [j for j in range(2)]
print(temp)
#testing = [[j for j in range(2)] for i in range(5)]
testing = [temp for i in range(5)]
print(testing)
#testing = [list(range(2)) for i in range(5)]
#print(testing)
