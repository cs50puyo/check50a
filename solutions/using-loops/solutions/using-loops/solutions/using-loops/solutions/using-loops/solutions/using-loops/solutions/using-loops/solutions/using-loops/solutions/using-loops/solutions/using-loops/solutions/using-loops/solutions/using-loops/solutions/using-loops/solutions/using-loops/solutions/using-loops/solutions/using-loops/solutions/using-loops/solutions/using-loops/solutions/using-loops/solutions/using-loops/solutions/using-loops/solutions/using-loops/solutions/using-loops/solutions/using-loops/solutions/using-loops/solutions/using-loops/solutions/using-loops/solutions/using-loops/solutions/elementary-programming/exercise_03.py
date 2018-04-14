mass = eval(input('Enter the amount of water in kilograms: '))
initial_temperature = eval(input('Enter the initial temperature: '))
final_temperature = eval(input('Enter the final temperature: '))

energy = mass * (final_temperature - initial_temperature) * 4184

print('The energy needed is', energy)
