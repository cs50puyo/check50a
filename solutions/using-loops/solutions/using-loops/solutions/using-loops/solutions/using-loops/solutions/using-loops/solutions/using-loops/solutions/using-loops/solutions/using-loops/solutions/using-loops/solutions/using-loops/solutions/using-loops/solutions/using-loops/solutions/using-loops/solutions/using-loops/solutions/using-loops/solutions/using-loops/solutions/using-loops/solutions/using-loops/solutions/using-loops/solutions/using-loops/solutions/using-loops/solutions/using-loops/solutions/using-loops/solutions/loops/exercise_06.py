lines = 8

for i in range(lines):
    for j in range(lines - 1, -1, -1):
        if j > i:
            print('    ', end='')

    for j in range(i + 1):
        print('{:4d}'.format(2 ** j), end='')

    for j in range(i - 1, -1, -1):
        print('{:4d}'.format(2 ** j), end='')

    print()
