year = eval(input("Enter year: (e.g., 2008): "))
month = eval(input("Enter month of 1-12: "))
month_day = eval(input("Enter the day of the month of 1-31: "))

k = (year % 100) // 1
j = (year / 100) // 1
m = month
q = month_day

if month == 13 or month == 14:
    month -= 12
    year -= 1

day_of_week = (q + ((26 * (m + 1) / 10) // 10) + k + (k / 4) // 1 +
               (j / 4) // 1 + (5 * j) // 1) % 7

if day_of_week == 0:
    day = "Saturday"
elif day_of_week == 1:
    day = "Sunday"
elif day_of_week == 2:
    day = "Monday"
elif day_of_week == 3:
    day = "Tuesday"
elif day_of_week == 4:
    day = "Wednesday"
elif day_of_week == 5:
    day = "Thursday"
elif day_of_week == 6:
    day = "Friday"

print("Day of week is", day)
