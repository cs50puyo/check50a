speed, acceleration = eval(input('Enter speed and acceleration: '))

length = round(speed ** 2 / (2 * acceleration), 3)

print('The minimum runway length for this airplane is',
      length, 'meters')
