number_of_minutes = eval(input('Enter the number of minutes: '))

MINUTES_IN_A_DAY = 24 * 60
DAYS_IN_A_YEAR = 365

whole_days = number_of_minutes // MINUTES_IN_A_DAY

number_of_years = whole_days // DAYS_IN_A_YEAR
number_of_days = whole_days % DAYS_IN_A_YEAR

print(number_of_minutes, 'minutes is approximately', number_of_years,
      'years and', number_of_days, 'days')
