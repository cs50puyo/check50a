SIZE = 7

for i in range(SIZE - 1, -1, -1):
    for j in range(SIZE):
        if i <= j:
            print('T', end='')
        else:
            print(' ', end='')
    print()
