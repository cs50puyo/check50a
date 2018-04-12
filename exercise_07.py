number = eval(input("Enter a three-digit integer: "))

digit_01 = number // 100
digit_02 = number // 10 % 10
digit_03 = number % 10

if digit_01 == digit_03:
    print(number, "is an palindrome")
else:
    print(number, "is not a palindrome")
