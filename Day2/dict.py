fruits = ['orange', 'watermelon', 'grapes', 'mango', 'apple']
price = [100, 120, 90, 230, 200]

# fruits          |   Min Price     | Max Price
# ____________________________________________ 
# orange          |   100           | 123
# watermelon      |   120           | 345
# grapes          |   90            | 355
# mango           |   230           | 467
# apple           |   200           | 574

# empty dict
price_of_fruits = {}
print(price_of_fruits, type(price_of_fruits))

# empty dict
price_of_fruits = dict()
print(price_of_fruits, type(price_of_fruits))

# dict = {key:value}
price_of_fruits = {
    'orange': 100,
    'watermelon': 120,
    'grapes': 90,
    'mango': 230,
    'apple': 200
}

print(price_of_fruits)

# get price(value) of orange
orange_price = price_of_fruits['orange']
print(orange_price)

# get price(value) of apple using get method
apple_price = price_of_fruits.get('apple')
print(apple_price)

# defining list with min and max price for fruit
min_max_price = {
    'orange': [100, 123],
    'watermelon': [120, 345],
    'grapes': [90, 355]
}

print(min_max_price)

# get list of keys and values of min_max_price
keys = min_max_price.keys()
values = min_max_price.values()

print(keys, values)

# get value of mango
min_max_price['mango'] = [120, 200]
print(min_max_price)
