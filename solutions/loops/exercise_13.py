import random

NUMBER_OF_TRIALS = 1000000
number_of_hits = 0

for _ in range(NUMBER_OF_TRIALS):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1

    area_one = -1 <= x <= 0 and -1 <= y <= 1
    area_three = x >= 0 and y >= 0 and y <= -x + 1

    if area_one or area_three:
        number_of_hits += 1

probability = number_of_hits / NUMBER_OF_TRIALS

print('The probability of the dart to fall into an'
      f'odd-numbered region is {probability}.')
