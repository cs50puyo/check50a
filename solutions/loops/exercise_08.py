END = 100000
pi_approx = 0

for i in range(1, END + 1):
    pi_approx += 4 * (-1) ** (i + 1) / (2 * i - 1)
    if i % 10000 == 0:
        print(f'The value of pi for i = {i} is {pi_approx}.')
