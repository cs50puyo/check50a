n = eval(input('Enter an integer: '))
divisor = 2

while n > 1:
    if n % divisor == 0:
        n /= divisor

        if n == 1:
            print(divisor)
        else:
            print(divisor, end=', ')
    else:
        divisor += 1
