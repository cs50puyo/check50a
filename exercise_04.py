num_01, num_02 , num_03 = eval(input("Enter three edges: "))

total_1_and_2 = num_01 + num_02
total_1_and_3 = num_01 + num_03
total_2_and_3 = num_02 + num_03
perimeter = num_01 + num_02 + num_03

if total_1_and_2 > num_03 and total_1_and_3 > num_02 and total_2_and_3 > num_01:
    print("The perimeter is:", perimeter)
else:
    print("Invalid input")
