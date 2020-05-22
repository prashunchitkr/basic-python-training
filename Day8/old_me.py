# I will create a list of fruits/vegetables to buy
# I will go to market and see discount prices

# This file do not use modules

# defining functions that operates on list to buy
def add_fruit(fruit, my_list):

    if fruit not in my_list:
        my_list.append(fruit)
        print('{} added to list'.format(fruit))
    else:
        print('{} already in list'.format(fruit))

    return my_list


def remove_fruit(fruit, my_list):

    if fruit in my_list:
        my_list.remove(fruit)
        print('{} removed from list'.format(fruit))
    else:
        print('{} not in list'.format(fruit))

    return my_list


def add_vegetable(vegetable, my_list):
    if vegetable not in my_list:
        my_list.append(vegetable)
        print('{} added to list'.format(vegetable))
    else:
        print('{} already in list'.format(vegetable))

    return my_list


def remove_vegetable(vegetable, my_list):
    if vegetable in my_list:
        my_list.remove(vegetable)
        print('{} removed from list'.format(vegetable))
    else:
        print('{} not in list'.format(vegetable))
    return my_list


# marked prices of fruits and vegetables
price_of_foods = {
    'orange': 100,
    'watermelon': 200,
    'grapes': 300,
    'tomato': 100,
    'potato': 400
}


# this function belongs to shop
def discount(my_list, discount=0.10):
    """
    this function returns price after discount
    """
    discount_rate = discount

    selling_price = {}

    for fruit in my_list:
        marked_price = price_of_foods[fruit]
        discount_amount = marked_price * discount_rate
        price = marked_price - discount_amount
        selling_price[fruit] = price

    return selling_price


# doing some food listing before going to shop
list_to_buy = []

add_fruit('orange', list_to_buy)
add_fruit('watermelon', list_to_buy)
add_fruit('grapes', list_to_buy)
remove_fruit('orange', list_to_buy)  # I don't like oranges
add_vegetable('tomato', list_to_buy)
add_vegetable('potato', list_to_buy)

# how much each costs after discount?
print(discount(list_to_buy))
