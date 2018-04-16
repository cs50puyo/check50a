binary_number = input('Enter a binary number: ')

decimal_number = 0
valid_binary = True
max_power = len(binary_number) - 1
for bit, power in zip(binary_number, range(max_power, -1, -1)):
    if not(bit == '0' or bit == '1'):
        valid_binary = False
        break
    else:
        bit = int(bit)
        decimal_number += bit * 2 ** power

if valid_binary:
    print(f'The binary number {binary_number} is {decimal_number} in decimal.')
else:
    print('Invalid binary number!')
