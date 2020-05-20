def check(num):
    if num%2 == 0:
        return True
    else:
        return False


def test(f):
    return f(4)

# f = check
# f(1)
print(test(check))

#filter option takes func iterable
print(list(filter(check, [1, 3, 4, 5, 6])))
