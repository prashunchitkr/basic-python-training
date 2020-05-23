
#hoc
#to_display = 'hello'

def display(to_display):
    def inner_fun():
        print('this is the value to print: ', to_display)
    return inner_fun

#closure
lets_display = display('hello world')
lets_display()

#normal func:
def normal_func(b):
    a = 2
    print(a)

normal_func('abcd')
#print(b)
