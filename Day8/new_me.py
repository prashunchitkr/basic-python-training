# I will create a list of fruits to buy
# I will go to market and see discount prices
# This file uses modules

import sys

# from packages.list import *

# absolute imports
from packages.list.fruits import add_fruit, remove_fruit
# can also be done by assigning object to a variable
from packages.list import vegetables as veg
from packages.shop.price import discount

# more ways to import
# import packages.list.fruits
# from packages.list.vegetables import add_vegetable, remove_vegetable


# lets get started

# checking available objects in this scope
print(dir())

# python searches for modules in paths available in sys.path
print(sys.path)

# doing some food listing before going to shop
list_to_buy = []

add_fruit('orange', list_to_buy)
add_fruit('watermelon', list_to_buy)
add_fruit('grapes', list_to_buy)
remove_fruit('orange', list_to_buy)  # I don't like oranges let's remove

veg.add_vegetable('tomato', list_to_buy)
veg.add_vegetable('potato', list_to_buy)

# how much each costs after discount?
print(discount(list_to_buy))
