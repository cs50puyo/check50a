first_int, second_int, third_int = eval(input("Enter 3 integer numbers: "))

if first_int >= second_int and first_int >= third_int:
    if second_int > third_int:
        print(third_int, second_int, first_int)
    elif second_int <= third_int:
        print(second_int, third_int, first_int)
elif second_int > first_int and second_int >= third_int:
    if first_int > third_int:
        print(third_int, first_int, second_int)
    elif first_int <= third_int:
        print(first_int, third_int, second_int)
elif third_int >= second_int and third_int >= first_int:
    if second_int >= first_int:
        print(first_int, second_int, third_int)
else:
    print(second_int, first_int, third_int)
