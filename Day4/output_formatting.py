# String Formatting

# using concatination
weekday = 'Monday'
text = 'Today is ' + weekday
print(text)

text = 'One ' + 'two' + 'three'
print(text)

var = 2
text = 'One ' + str(var) + 'Three'
print(text)

# using {}
text = 'Today is {}'.format(weekday)
print(text)

text = '{} two {}'.format('one', 'two')
print(text)

text = '{1} two {0}'.format('one', 'two')
print(text)

text = '{one} two {two}'.format(one='one', two='two')
print(text)

# using f-strings
text = f'Today is {weekday}'
print(text)

one = 1.1214133132
two = 2
text = f"{round(one,2)} two {two}"
print(text)

# using in print statement
print('today is', weekday)
print(f'Today is {weekday}')
