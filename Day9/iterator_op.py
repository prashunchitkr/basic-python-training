
#iterator and iterable

#this is iterable
i = [1, 2, 3, 4, 5]
#next(i)
#print(dir(i))

#this is iterator
i_iterator = i.__iter__()
#i_iterator = iter(i)
#print('\n\n\n')
#print(dir(i_iterator))


#all iterable objects can produce an iterator object but they itself are not an iterator
print(next(i_iterator))
print(next(i_iterator))
print(i_iterator.__next__())
print(i_iterator.__next__())
print(i_iterator.__next__())
#print(i_iterator.__next__())


#while until we get stopIteration error

for temp in i:
    print(temp)

for i range(10):

