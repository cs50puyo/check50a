s = input('Enter a string: ')
phone_number = ''

for char in s:
    if char.isdigit() or char == '-':
        phone_number += char
    elif char.isalpha():
        char = char.upper()
        if char in 'ABC':
            phone_number+= '2'
        elif char in 'DEF':
            phone_number+= '3'
        elif char in 'GHI':
            phone_number+= '4'
        elif char in 'JKL':
            phone_number+= '5'
        elif char in 'MNO':
            phone_number+= '6'
        elif char in 'PQRS':
            phone_number+= '7'
        elif char in 'TUV':
            phone_number+= '8'
        elif char in 'WXYZ':
            phone_number+= '9'

print(phone_number)
