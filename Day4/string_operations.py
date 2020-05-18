'''
String Operations
1. List analogy
2. count()
3. split()
4. startswith()/endswith()
5. Repeating strings
6. replace()
7. upper()/lower()
8. strip()/lstrip()/rstrip()
9. join()
'''


text = 'Hello World'

print(text[:5])

for char in text:
    print(char)


# .count()
print(text.count('Hello'))


# .split()
print(text.split(' '))
print(text.split('l'))
text = input("Enter a string: ")
print(text.split(' '))


# .startswith()/endswith()
print(text.startswith('Hel'))
print(text.startswith('asda'))
print(text.endswith('rld'))


# repeating strings
print(f'test {text}' * 10)

# Replace
print(text.replace('World', 'Class'))


# upper() lower()
print(text.upper())


# strip() lstrip() rstrip()
text = '      some text         '
print(text.strip())
print(text.lstrip())
print(len(text.lstrip()))
print(text.rstrip())


# join()
some_arr = ['This', 'Is', 'A', 'Test', 'String']
print('\n'.join(some_arr))
text = 'apple'
print(':'.join(text))


# string reverse
print(text[::-1])
