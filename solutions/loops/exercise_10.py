END = 10000

for i in range(6, END + 1):
    divisor_sum = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            divisor_sum += j

    if i == divisor_sum:
        print(f'{i} is a perfect number.')
