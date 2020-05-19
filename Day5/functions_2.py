# list_to_buy list should always be available
list_to_buy = []

def add_fruit(fruit):

    f = fruit

    if f not in list_to_buy:
        list_to_buy.append(f)
        print('{} added to list'.format(f))
    else:
        print('{} already in list'.format(f))


def remove_fruit(fruit):

    f = fruit
    
    if f in list_to_buy:
        list_to_buy.remove(f)
        print('{} removed from list'.format(f))
    else:
        print('{} not in list'.format(f))

# first class function
fruit = add_fruit
fruit('orange')

add_fruit('orange')
add_fruit('watermelon')
add_fruit('grapes')
remove_fruit('orange')
fruit('watermelon')

print(list_to_buy)