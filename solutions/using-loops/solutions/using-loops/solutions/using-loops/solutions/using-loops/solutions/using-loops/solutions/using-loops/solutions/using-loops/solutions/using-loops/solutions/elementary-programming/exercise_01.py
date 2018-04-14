number = eval(input('Enter a number between 0 and 1000: '))

units = number % 10
number //= 10
tens = number % 10
number //= 10
hundreds = number % 10
number //= 10
thousands = number % 10

print('The sum of the digits is ', units + tens + hundreds + thousands)
