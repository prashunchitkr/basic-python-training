'''
Set Operations:
1. Union
2. Inersection
3. Difference
4. Symmetric Difference
5. issuperset()
6. issubset()
'''

basket = {'orange', 'apple', 'grape'}
shelf = {'apple', 'pear'}

# intersection
print(basket.intersection(shelf))
print(basket & shelf)

# union
print(basket.union(shelf))
print(basket | shelf)

# A - B
print(basket.difference(shelf))
print(basket - shelf)

# not(AnB)
print(basket.symmetric_difference(shelf))
print(basket ^ shelf)


# superset and subset
basket = {'apple'}
shelf = {'apple', 'grape', 'orange'}

print(basket.issubset(shelf))
print(shelf.issubset(basket))

print(shelf.issuperset(basket))
print(basket.issuperset(shelf))
