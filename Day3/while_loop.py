
#values should exist before updating it
c = 10
c = c + 1

while(c > 0):
    print('test')
    c = c - 1

# while True:
#     print('this is infinite loop pess ctrl c or kill the window to exit')

n = 2
c = 1
while(True):
    n = n* 2
    c = c + 1
    if n > 12345:
        print('exited', c)
    

#break
a = 5
while a > 0:
    print(a)
    if a == 2:
        break
    a = a - 1

#continue
a = 10
while a > 0:
    if a%2 != 0:
        a = a - 1
        continue
    print(a)
    a = a- 1