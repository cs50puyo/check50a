number_of_month = eval(input("Enter the number of month: "))
year = eval(input("Enter the year: "))

if number_of_month == 1:
    days = 31
    month = "January"
elif number_of_month == 2:
    month = "February"
    if year % 4 == 0:
        days = 29
    else:
        days= 28
elif number_of_month == 3:
    month = "March"
    days = 30
elif number_of_month == 4:
    days= 30
    month = "April"
elif number_of_month == 5:
    days= 31
    month = "May"
elif number_of_month == 6:
    days= 30
    month = "June"
elif month == 7:
    days = 31
    month = "July"
elif month == 8:
    days_of_month = 31
    month = "August"
elif number_of_month == 9:
    days = 30
    month = "September"
elif number_of_month == 10:
    days = 31
    month = "October"
elif number_of_month == 11:
    days = 30
    month = "November"
elif number_of_month == 12:
    days = 31
    month = "December"


print(month, "of", year, "have", days)
