number = eval(input('Enter a number (0: for end of input): '))
largest_number = number
counter = 1

if number != 0:
    while True:
        number = eval(input('Enter a number (0: for end of input): '))

        if number == 0:
            break

        if number > largest_number:
            largest_number = number
            counter = 1
        elif number == largest_number:
            counter += 1

    print(f'The largest number is {largest_number}.')
    print(f'The occurrence count of the largest number is {counter}.')
