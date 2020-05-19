price_of_fruits = {
    'orange': 100,
    'watermelon': 200,
    'grapes': 300
}

# shopkeeper started giving discount on every fruit with 10% as default
# discount is a default argument for function
def discount(fruit, discount=0.10):
    # explaing function using docstring
    """
    this function returns price after discount
    """
    discount_rate = discount
    marked_price = price_of_fruits[fruit]

    discount_amount = marked_price * discount_rate
    price = marked_price - discount_amount

    return price

print(discount.__doc__)
print(discount('orange'))
print(discount('orange', 0.60))
print(discount('orange', discount=0.60))