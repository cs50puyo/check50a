day = eval(input('Enter today\'s day: '))
days_elapsed = eval(input('Enter the number of days elapsed since today: '))

future_day = (day + days_elapsed) % 7

if day == 0:
    day_name = 'Sunday'
elif day == 1:
    day_name = 'Monday'
elif day == 2:
    day_name = 'Tuesday'
elif day == 3:
    day_name = 'Wednesday'
elif day == 4:
    day_name = 'Thursday'
elif day == 5:
    day_name = 'Friday'
else:
    day_name = 'Saturday'

if future_day == 0:
    future_day_name = 'Sunday'
elif future_day == 1:
    future_day_name = 'Monday'
elif future_day == 2:
    future_day_name = 'Tuesday'
elif future_day == 3:
    future_day_name = 'Wednesday'
elif future_day == 4:
    future_day_name = 'Thursday'
elif future_day == 5:
    future_day_name = 'Friday'
else:
    future_day_name = 'Saturday'

print(f'Today is {day_name} and the future day is {future_day_name}')
