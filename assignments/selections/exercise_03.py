month = eval(input('Enter the month: '))
year = eval(input('Enter the year: '))

if month == 1:
    month_name = 'January'
    days = 31
elif month == 2:
    month_name = 'February'
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days = 29
    else:
        days = 28
elif month == 3:
    month_name = 'Marh'
    days = 31
elif month == 4:
    month_name = 'April'
    days = 30
elif month == 5:
    month_name = 'May'
    days = 31
elif month == 6:
    month_name = 'June'
    days = 30
elif month == 7:
    month_name = 'July'
    days = 31
elif month == 8:
    month_name = 'August'
    days = 31
elif month == 9:
    month_name = 'September'
    days = 30
elif month == 10:
    month_name = 'October'
    days = 31
elif month == 11:
    month_name = 'November'
    days = 30
else:
    month_name = 'December'
    days = 31

print(f'{month_name} has {days} days.')
