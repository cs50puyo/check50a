total = 0
for i in range(1, 625):
    total += 1 / (i ** 0.5 + (i + 1) ** 0.5)

print(f'The total of the summation is {total}')
