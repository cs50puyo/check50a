hex_character = str(input("Enter a hex character: "))

if hex_character == "a" or hex_character == "A":
    print('The decimal value is 10')
elif hex_character == "b" or hex_character == "B":
    print("The decimal value is 11")
elif hex_character == "c" or hex_character == "C":
    print("The decimal value is 12")
elif hex_character == "d" or hex_character == "D":
    print("The decimal value is 13")
elif hex_character == "e" or hex_character == "E":
    print("The decimal value is 14")
elif hex_character == "f" or hex_character == "F":
    print("The decimal value is 15")
elif hex_character > chr(70):
    print("Invalid input")
elif int(hex_character) >= 0 and int(hex_character) <= 9:
    print("The decimal value is", hex_character)
else:
    print("Invalid input")
