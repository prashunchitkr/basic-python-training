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


if __name__ == "__main__":
    print('you should import this module \n do not use directly')
