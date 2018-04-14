rat_1_weight = 10
rat_2_weight = 10

rat_1_rate = 4
rat_2_rate = 3

weeks = 0

while rat_1_weight < 1.1 * rat_2_weight:
    rat_1_weight += rat_1_weight * rat_1_rate / 100
    rat_2_weight += rat_2_weight * rat_2_rate / 100
    weeks += 1

print(f'{weeks} are required to make rat_1 10% heavier than rat_2',
      f'if rat_1\'s rate is {rat_1_rate}% and rat_2\'s rate is {rat_2_rate}%.')
