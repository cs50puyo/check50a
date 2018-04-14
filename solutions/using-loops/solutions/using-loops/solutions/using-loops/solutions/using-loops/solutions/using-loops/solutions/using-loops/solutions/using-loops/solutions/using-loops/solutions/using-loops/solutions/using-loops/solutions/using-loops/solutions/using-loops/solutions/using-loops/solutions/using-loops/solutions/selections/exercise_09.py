hex = input('Enter a hex character: ')
hex = hex.upper()
text = 'The decimal value is {}'

if 'A' <= hex <= 'F':
    decimal = 10 + int(ord(hex) - ord('A'))
    print(text.format(decimal))
elif '0' <= hex <= '9':
    decimal = int(hex)
    print(text.format(decimal))
else:
    print('Invalid input')
