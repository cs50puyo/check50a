END = 7
combinations = 0

for i in range(1, END + 1):
    for j in range(i + 1, END + 1):
        combinations += 1
        print(i, j)

print(f'The total number of all combinations is {combinations}.')
