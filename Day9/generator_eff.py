#0 1 1 2 3 5 8 13

def fibonacci():
   x, y = 0, 1
   while True:
       yield x
       x, y = y, x+y


#fibo = fibonacci()
#print(next(fibo))
#print(next(fibo))
#print(next(fibo))
#print(next(fibo))
#for i in range(10):
#    print(next(fibo))

#for i in fibonacci():
#    print(i)

#generator comprehension
#()

sq_num = (i**2 for i in range(100))
for i in range(10):
    print(next(sq_num))

