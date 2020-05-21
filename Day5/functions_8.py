test_list = list(range(14))

def square(x):
    return x*x

print(list(map(square, test_list)))


# defining own map function
def my_map(f, l):
    
    new_list = []

    for i in l:
        new_list.append(f(i))
    return new_list

print(my_map(square, test_list))


def is_even(x):
    if x%2 == 0:
        return True
    return False

# get even list
print(list(filter(is_even, test_list)))

# get odd list
print(list(filter(lambda x: not is_even(x), test_list)))


# defining own filter function
def my_filter(f, l):
    new_list = []

    for i in l:
        if f(i):
            new_list.append(i)
    return new_list

print(my_filter(is_even, test_list))


# returning function from function depending on argument passed
def odd_even(n):    
    def odd():
        return 'you are odd bro'
    def even():
        return 'we all are even here'
    
    if n%2 == 0:
        return even
    else:
        return odd

# check variable will be pointing to either even or odd function
check = odd_even(11) # odd in this case
print(check())


