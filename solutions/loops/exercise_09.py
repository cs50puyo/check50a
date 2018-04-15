END = 100000
e_approx = 1
factorial = 1

for i in range(1, END + 1):
    factorial *= i
    e_approx += 1 / factorial

    if i % 10000 == 0:
        print(f'The value of e for i = {i} is {e_approx}.')
