ISBN_number = input('Enter the first 9 digits of an ISBN-10 as a string: ')
total = 0

for digit, factor in zip(ISBN_number, range(1, 10)):
    total += int(digit) * factor

check_sum = total % 11
last_digit = 'X' if check_sum == 10 else str(check_sum)

print(f'The ISBN-10 number is {ISBN_number + str(last_digit)}')
