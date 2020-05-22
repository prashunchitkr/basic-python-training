price_of_foods = {
    'orange': 100,
    'watermelon': 200,
    'grapes': 300,
    'tomato': 100,
    'potato': 400
}


# I am more happy here
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
