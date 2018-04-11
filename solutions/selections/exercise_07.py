number = input('Enter a three-digit integer: ')

if number == number[::-1]:
    print(number, 'is a palindrome')
else:
    print(number, 'is not a palindrome')
