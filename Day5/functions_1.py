list_to_buy = []

# defining each functions for adding and removing every fruits

def add_orange():

    orange = 'orange'
    
    if orange not in list_to_buy:
        list_to_buy.append(orange)
        print('{} added to list'.format(orange))
    else:
        print('{} already in list'.format(orange))


def add_watermelon():

    watermelon = 'watermelon'
    
    if watermelon not in list_to_buy:
        list_to_buy.append(watermelon)
        print('{} added to list'.format(watermelon))
    else:
        print('{} already in list'.format(watermelon))


def remove_orange():

    orange = 'orange'
    
    if orange in list_to_buy:
        list_to_buy.remove(orange)
        print('{} removed from list'.format(orange))
    else:
        print('{} not in list'.format(orange))


add_orange()
add_orange()
add_watermelon()
remove_orange()
print(list_to_buy)