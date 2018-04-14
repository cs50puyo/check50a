monthly_savings = eval(input('Enter the monthly saving amount: '))

ANNUAL_INTEREST_RATE = 5 / 100
MONTHLY_INTEREST_RATE = ANNUAL_INTEREST_RATE / 12
FACTOR = (1 + MONTHLY_INTEREST_RATE)

amount = 0

# first month
amount = (monthly_savings + amount) * FACTOR
# second month
amount = (monthly_savings + amount) * FACTOR
# third month
amount = (monthly_savings + amount) * FACTOR
# fourth month
amount = (monthly_savings + amount) * FACTOR
# fifth month
amount = (monthly_savings + amount) * FACTOR
# sixth month
amount = (monthly_savings + amount) * FACTOR

print('After the sixth month, the account value is', round(amount, 2))
