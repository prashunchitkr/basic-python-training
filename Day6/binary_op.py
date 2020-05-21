with open('diff_encode.txt', 'rb') as f:
    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.read().decode('cp437'))


with open('testing.txt', 'w', encoding='UTF-16') as f:
    f.write('lasdjfkldsajfk;dsa;kfjklsdjf')
    #UTF-16