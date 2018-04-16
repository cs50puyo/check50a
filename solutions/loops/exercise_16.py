NUMBERS = 10
print('Enter ten numbers: ', end='')
total = 0
square_sum = 0

for _ in range(NUMBERS):
    number = eval(input())
    total += number
    square_sum += number ** 2

mean = total / NUMBERS
std_deviation = ((square_sum - mean ** 2 * NUMBERS) / (NUMBERS - 1)) ** 0.5

print(f'The mean is {mean}')
print(f'The standard deviation is {std_deviation}')
