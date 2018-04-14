lines = 8

for i in range(lines):
    # initial spacing
    for j in range(lines - 1, -1, -1):
        if j > i:
            print('    ', end='')

    # first part of the pyramid
    for j in range(i + 1):
        print('{:4d}'.format(2 ** j), end='')

    # second part of the pyramid
    for j in range(i - 1, -1, -1):
        print('{:4d}'.format(2 ** j), end='')

    print()
