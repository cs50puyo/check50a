ISBN_number = input('Enter the first 12 digits of an ISBN-13 as a string: ')
total = 0

for digit, i in zip(ISBN_number, range(1, 13)):
    total += int(digit) if i % 2 == 1 else 3 * int(digit)

check_sum = 10 - total % 10
last_digit = '0' if check_sum == 10 else str(check_sum)

print(f'The ISBN-10 number is {ISBN_number + str(last_digit)}')
