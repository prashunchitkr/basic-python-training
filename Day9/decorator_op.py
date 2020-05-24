def decorator_fun(func):
    def inner_fun(a):
        print('function is decorated')
        func(a)
    return inner_fun


#def display(a):
#    print(a)

#display(7)
#decorated = decorator_fun(display)
#decorated(4)


#decorators

def dash(func):
    def inner_fun(*args, **kwargs):
        print('--'*20)
        func(*args, **kwargs)
        print('--'*20)

    return inner_fun

def check_even(func):
    def inner_fun(*args, **kwargs):
        for i in args:
            if i%2 == 0:
                func('even')
            else:
                func('odd')
    return inner_fun

#display = check_even(display)
#display(9)


#@check_name

@dash
@check_even
def display(a):
    print(a)

display(2, 23, 4, 2)

#nested decorator
#display = dash(check_even(display))


