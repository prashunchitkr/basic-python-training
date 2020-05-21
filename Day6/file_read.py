'''
mode:
r
w
a
b
'''

filehandler = open('first.txt', 'w')
filehandler.write('hello world')
filehandler.close()


filehandler = open('first.txt', 'r')
print(filehandler.read())

#writelines
temp = ['firstline\n', 'secondline\n', 'thirdline\n']
filehandler = open('first.txt', 'w')
# filehandler.write('hello world\nsecond line\nthird line')
filehandler.writelines(temp)
filehandler.close()

filehandler = open('first.txt', 'r')
for i in filehandler:
    print(i)
filehandler.close()

filehandler = open('first.txt', 'r')
print(filehandler.readline())
print(filehandler.readline())
filehandler.close()

#with
with open('first.txt', 'r') as f:
    print(f.read())

#read plus write
with open('first.txt', 'r+') as f:
    print(f.read())
    f.write('hello world')
    f.seek(0)
    print('after write')
    print(f.read())

#'' EOF
with open('first.txt', 'r+') as f:
    print(f.read(4), end='')
    print(f.read(4))
    print(f.read())
    print('the cursor is in line: ', f.tell())
    f.seek(0)
    print('the cursor is in line: ', f.tell())
    print(f.read())

# def something():
#     pass

with open('first.txt', 'r+') as f:
    print(f.readlines())
    print('the cursor is in line: ', f.tell())
    print(f.read(6))

#read lines
with open('first.txt', 'r+') as f:
    print(f.readline())

