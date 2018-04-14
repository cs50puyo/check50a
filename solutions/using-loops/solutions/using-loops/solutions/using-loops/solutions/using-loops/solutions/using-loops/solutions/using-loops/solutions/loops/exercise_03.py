n1 = eval(input('Enter first integer: '))
n2 = eval(input('Enter second integer: '))

d = min(n1, n2)

for i in range(d, 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        break

print(f'The greatest common divisor is {i}.')
