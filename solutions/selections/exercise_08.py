x, y = eval(input('Enter a point\'s x- and y-coordinates: '))

if x >= 0 and y >= 0 and y <= (-1 / 2) * x + 100:
    print('The point is in the triangle')
else:
    print('The point is not in the triangle')
