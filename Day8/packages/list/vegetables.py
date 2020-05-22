# absolute importing of modules
# from packages.list.fruits import add_fruit
# from packages.shop.price import discount

# relative importing of modules
# from .fruits import add_fruit
# from ..shop.price import discount

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
