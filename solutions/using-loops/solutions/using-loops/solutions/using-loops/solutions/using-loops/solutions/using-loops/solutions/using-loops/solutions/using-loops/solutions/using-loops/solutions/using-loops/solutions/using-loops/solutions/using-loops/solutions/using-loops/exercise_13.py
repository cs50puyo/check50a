SIZE = 7

for i in range(SIZE):
    for j in range(SIZE):
        if i >= j:
            print('T', end='')
    print()
