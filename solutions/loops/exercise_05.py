lines = eval(input('Enter number of lines: '))

for i in range(1, lines + 1):
    # initial spacing
    if lines >= 10:
        spacing = lines - 9 if 1 <= i <= 9 else lines - i
        print(' ' * spacing, end='')

    # first part of the pyramid
    for j in range(lines, 0, -1):
        if i >= j:
            print(j, end=' ')
        else:
            print('  ', end='')

    # second part of the pyramid
    for j in range(2, i + 1):
        if j < i:
            print(j, end=' ')
        elif j == i:
            print(j, end='')

    print()
