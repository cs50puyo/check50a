today_number = eval(input("Enter today's day: "))
future_day = eval(input("Enter the number of days elapsed since today: "))

if today_number == 0:
    today = "Sunday"
elif today_number == 1:
    today = "Monday"
elif today_number == 2:
    today = "Tuesday"
elif today_number == 3:
    today = "Wednesday"
elif today_number == 4:
    today = "Thursday"
elif today_number == 5:
    today = "Friday"
elif today_number == 6:
    today = "Saturday"
else:
    print("")

future_day += today_number

if future_day == 0:
    future_day = "Sunday"
elif future_day == 1:
    future_day = "Mon"
elif future_day == 2:
    future_day = "Tuesday"
elif future_day == 3:
    future_day = "Wednesday"
elif future_day == 4:
    future_day = "Thursday"
elif future_day == 5:
    future_day= "Friday"
elif future_day == 6:
    future_day = "Saturday"
else:
    print("")

print("Today is", today, "and the future day is", future_day)
