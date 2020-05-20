prime_nums = []
num = 2
while len(prime_nums) < 100:
    for i in range(2, num):
        if num % i == 0:
            num += 1
            break
    else:
        prime_nums.append(num)
        num += 1
print(prime_nums)