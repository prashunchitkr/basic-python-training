import os

print(os.getcwd())
print(os.chdir('/home/siki/Documents/basic-python-training/Day5'))
# print(os.chdir('C:/nusers')) '\n \t\''
print(os.getcwd())

# with open('TODO.txt', 'r') as f:
#     print(f.read())

# os.mkdir('testdir')
# os.rmdir('testdir')
# os.remove('temp.txt')


# os.walk
# for i in os.walk('.'):
#     for j in i:
#         print(os.path.join('basic-python-training', j))
print(os.path.join('abc', 'def'))