rat_1_weight = 10
rat_1_rate = 4
rat_1_weight_25_percent = 1.25 * rat_1_weight
weeks = 0

while rat_1_weight < rat_1_weight_25_percent:
    rat_1_weight += rat_1_weight * rat_1_rate / 100
    weeks += 1

print(f'{weeks} are required to make rat_1 25% heavier at rate {rat_1_rate}%.')
