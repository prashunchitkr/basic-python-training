
'''
encoding
windows cp1252
linux UTF-8
mac UTF-8 UTF-16
'''

with open('first.txt', 'r', encoding='UTF-8') as f:
    print(f.encoding)
    print(f.read())
