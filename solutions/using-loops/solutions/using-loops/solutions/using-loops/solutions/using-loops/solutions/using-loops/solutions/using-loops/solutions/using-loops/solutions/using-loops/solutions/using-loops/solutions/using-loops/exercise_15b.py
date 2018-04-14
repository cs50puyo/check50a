SIZE = 7

i = SIZE - 1
while i >= 0:
    j = 0
    while j < SIZE:
        if i <= j:
            print('T', end='')
        else:
            print(' ', end='')
        j += 1
    i -= 1
    print()
