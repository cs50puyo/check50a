year = eval(input('Enter year: (e.g., 2008): '))
month = eval(input('Enter month: 1-12: '))
# q is the day of the month
q = eval(input('Enter the day of the month: 1-31: '))

if month == 1:
    month = 13
    year -= 1
elif month == 2:
    month = 14
    year -= 1

# j is the century
j = year // 100
# k is the year of the century
k = year % 100

h = (q + (26 * (month + 1) // 10) + k + k // 4 + j // 4 + 5 * j) % 7

text = 'Day of the week is {}'

if h == 0:
    print(text.format('Saturday'))
elif h == 1:
    print(text.format('Sunday'))
elif h == 2:
    print(text.format('Monday'))
elif h == 3:
    print(text.format('Tuesday'))
elif h == 4:
    print(text.format('Wednesday'))
elif h == 5:
    print(text.format('Thursday'))
else:
    print(text.format('Friday'))
