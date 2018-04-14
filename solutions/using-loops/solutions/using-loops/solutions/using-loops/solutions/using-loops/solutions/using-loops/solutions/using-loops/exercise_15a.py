SIZE = 7

i = 0
while i < SIZE:
    j = 0
    while j < SIZE:
        if i >= j:
            print('T', end='')
        j += 1
    i += 1
    print()
