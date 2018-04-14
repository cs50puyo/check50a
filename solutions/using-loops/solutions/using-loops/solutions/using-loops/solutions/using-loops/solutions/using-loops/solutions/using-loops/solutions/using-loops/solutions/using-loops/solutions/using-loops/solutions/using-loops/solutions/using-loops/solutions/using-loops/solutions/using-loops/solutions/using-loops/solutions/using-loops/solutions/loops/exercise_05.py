lines = eval(input('Enter number of lines: '))


for i in range(1, lines + 1):
    for j in range(10, lines + 1):
        if i < j:
            print(' ', end='')

    for j in range(lines, 0, -1):
        if i >= j:
            print(j, end=' ')
        else:
            print('  ', end='')

    for j in range(2, i + 1):
        if j < i:
            print(j, end=' ')
        elif j == i:
            print(j, end='')

    print()
