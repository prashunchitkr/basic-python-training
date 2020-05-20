# using multiple returns in function
def is_prime(n):
    if n==0 or n==1:
        return False

    for i in range(2, n):
        if n%i == 0:
            return False

    return True

print(is_prime(5))