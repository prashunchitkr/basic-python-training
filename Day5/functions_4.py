# packing
def add_to_list(*args):
    if args is not None:
        for f in args:
            print(f)

add_to_list('apple', 'papaya')


# unpacking
def add_to_bag(fruit_1, fruit_2, fruit_3):
    print(fruit_1, fruit_2, fruit_3)

fruits = ['orange', 'watermelon', 'apple']
add_to_bag(*fruits)


# packing
def add_to_basket(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

add_to_basket(orange=100, watermelon=200, grapes=300)


# unpacking
def add_to_jhola(orange, watermelon, grapes):
    print('{} {} {}'.format(
        orange,
        watermelon,
        grapes))

price_of_fruits = {
    'orange': 100,
    'watermelon': 200,
    'grapes': 300
}

add_to_jhola(**price_of_fruits)