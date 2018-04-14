amount = eval(input('Loan Amount: '))
years = eval(input('Number of years: '))

print('Interest Rate\tMonthly Payment\tTotal Payment')

interest_rate = 5
step = 1 / 8

while interest_rate <= 8:
    monthly_interest_rate = (interest_rate / 100) / 12
    monthly_payment = amount * monthly_interest_rate / \
                    (1 - 1 / (1 + monthly_interest_rate) ** (years * 12))
    total_payment = monthly_payment * years * 12

    print(f'{interest_rate:.3f}%\t\t'
          f'{round(monthly_payment, 2)}\t\t'
          f'{round(total_payment, 2)}')
    interest_rate += step
