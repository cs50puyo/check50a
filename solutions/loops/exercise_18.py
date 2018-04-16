binary = input('Enter a binary number: ')
len_bin = len(binary)

# Add zeros until number of bits is multiple of 4
remainder = len_bin % 4
binary = binary if remainder == 0 else (4 - remainder) * '0' + binary
hexadecimal = ''

for i in range(0, len_bin, 4):
    four_bits = binary[i: i + 4]
    decimal = 0
    for bit, exponent in zip(four_bits, range(3, -1, -1)):
        decimal += int(bit) * 2 ** exponent

    if 0 <= decimal <= 9:
        hexadecimal += str(decimal)
    else:
        hexadecimal += chr(ord('A') + (decimal - 10))

print(f'The binary number {binary} is {hexadecimal} in hexadecimal.')
