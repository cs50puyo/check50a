side1, side2, side3 = eval(input('Enter three edges: '))

pair_one = side1 + side2 > side3
pair_two = side1 + side3 > side2
pair_three = side2 + side3 > side1

if pair_one and pair_two and pair_three:
    print('The perimeter is', side1 + side2 + side3)
else:
    print('The input is invalid')
